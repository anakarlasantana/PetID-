# Generated by Django 5.1.4 on 2025-01-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("animals", "0003_rename_qr_data_rgrequest_qr_code_data_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rgrequest",
            old_name="tutor_contact",
            new_name="tutor_phone",
        ),
        migrations.AddField(
            model_name="rgrequest",
            name="tutor_address",
            field=models.CharField(default=None, max_length=500),
        ),
    ]