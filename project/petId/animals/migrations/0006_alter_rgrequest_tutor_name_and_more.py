# Generated by Django 5.1.4 on 2025-01-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0005_alter_rgrequest_tutor_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rgrequest",
            name="tutor_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="rgrequest",
            name="tutor_phone",
            field=models.CharField(max_length=100),
        ),
    ]
