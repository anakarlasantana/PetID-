# Generated by Django 5.1.4 on 2025-01-06 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimalType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("icon", models.ImageField(upload_to="animal_icons/")),
            ],
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("background", models.ImageField(upload_to="templates/")),
                ("has_qr_code", models.BooleanField(default=False)),
                ("has_tutor_info", models.BooleanField(default=True)),
                (
                    "animal_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animals.animaltype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RGRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("animal_photo", models.ImageField(upload_to="animal_photos/")),
                ("animal_name", models.CharField(max_length=100)),
                ("breed", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Macho", "Macho"), ("Fêmea", "Fêmea")],
                        default="Macho",
                        max_length=10,
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("tutor_name", models.CharField(max_length=100)),
                ("tutor_contact", models.CharField(max_length=100)),
                ("qr_data", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animals.template",
                    ),
                ),
            ],
        ),
    ]