from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="animal_icons/")

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=100)
    background = models.ImageField(upload_to="templates/")
    animal_type = models.ForeignKey(
        AnimalType, on_delete=models.CASCADE, null=True, blank=True
    )
    has_qr_code = models.BooleanField(default=False)
    has_tutor_info = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RGRequest(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    animal_photo = models.ImageField(upload_to="animal_photos/")
    animal_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=(("Macho", "Macho"), ("Fêmea", "Fêmea")),
        default="Macho"
    )
    birth_date = models.DateField(blank=True, null=True)
    tutor_name = models.CharField(max_length=100)
    tutor_contact = models.CharField(max_length=100)
    qr_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RG for {self.animal_name} ({self.tutor_name})"
