from rest_framework import serializers
from ..models.rg import Template, RGRequest


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class RGRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGRequest
        fields = '__all__'
