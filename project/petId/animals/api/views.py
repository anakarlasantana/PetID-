from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.rg import Template, RGRequest
from .serializers import TemplateSerializer, RGRequestSerializer
from utils.generate_rg import generate_rg


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class RGRequestViewSet(viewsets.ModelViewSet):
    queryset = RGRequest.objects.all()
    serializer_class = RGRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            rg_request = serializer.save()

            # Gerar o RG
            template_path = rg_request.template.background.path
            animal_photo_path = rg_request.animal_photo.path
            animal_icon_path = (
                rg_request.template.animal_type.icon.path
                if rg_request.template.animal_type
                else None
            )

            rg_path = generate_rg(
                template_path,
                animal_photo_path,
                rg_request.animal_name,
                rg_request.breed,
                rg_request.gender,
                rg_request.birth_date,
                rg_request.tutor_name,
                rg_request.tutor_contact,
                rg_request.qr_code_data,
                animal_icon_path,
            )

            return Response(
                {"message": "RG gerado com sucesso!", "rg_path": rg_path},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
