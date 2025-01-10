from rest_framework import serializers
from ..models.rg import Template, RGRequest


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"


class RGRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGRequest
        fields = "__all__"

    def validate(self, data):
        if data.get("qr_code_data") and not data.get("qr_code_image"):
            raise serializers.ValidationError(
                {
                    "qr_code_image": "QR Code image is required when QR Code data is enabled."
                }
            )
        return data
