from PIL import Image, ImageDraw, ImageFont
import qrcode
import os


def generate_rg(
    template_path,
    animal_photo_path,
    animal_name,
    breed,
    gender,
    birth_date,
    tutor_name,
    tutor_contact,
    qr_data=None,
    animal_icon_path=None,
):
    # Carregar o template base
    template = Image.open(template_path).convert("RGBA")
    width, height = template.size

    # Carregar a foto do animal e ajustar o tamanho
    animal_photo = Image.open(animal_photo_path).convert("RGBA")
    animal_photo = animal_photo.resize(
        (int(width * 0.3), int(height * 0.3))
    )  # Ajustar tamanho da foto
    template.paste(animal_photo, (50, 100), animal_photo)  # Posição relativa

    # Adicionar o ícone do tipo de animal, se fornecido
    if animal_icon_path:
        animal_icon = Image.open(animal_icon_path).convert("RGBA")
        animal_icon = animal_icon.resize((100, 100))  # Ajustar tamanho do ícone
        template.paste(animal_icon, (width - 150, 50), animal_icon)

    # Adicionar informações do animal e tutor
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype("arial.ttf", 20)  # Ajuste para o caminho da fonte Arial

    # Informações do animal
    draw.text((50, 300), f"Nome: {animal_name}", fill="black", font=font)
    draw.text((50, 340), f"Raça: {breed}", fill="black", font=font)
    draw.text((50, 380), f"Gênero: {gender}", fill="black", font=font)
    draw.text((50, 420), f"Nascimento: {birth_date}", fill="black", font=font)

    # Informações do tutor
    draw.text((50, 460), f"Tutor: {tutor_name}", fill="black", font=font)
    draw.text((50, 500), f"Contato: {tutor_contact}", fill="black", font=font)

    # Adicionar QR Code, se necessário
    if qr_data:
        qr = qrcode.make(qr_data)
        qr = qr.resize((150, 150))  # Ajustar tamanho do QR Code
        template.paste(qr, (width - 200, height - 200), qr)

    # Salvar o RG gerado
    output_path = os.path.join("generated", f"rg_{animal_name}.png")
    template.save(output_path, "PNG")
    return output_path
