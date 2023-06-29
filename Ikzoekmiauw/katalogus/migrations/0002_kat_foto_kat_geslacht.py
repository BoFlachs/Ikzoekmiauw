# Generated by Django 4.2.2 on 2023-06-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("katalogus", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="kat",
            name="foto",
            field=models.ImageField(null=True, upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AddField(
            model_name="kat",
            name="geslacht",
            field=models.CharField(
                choices=[
                    ("Man", "Mannelijk"),
                    ("Vrouw", "Vrouwelijk"),
                    ("Onbekend", "Onbekend"),
                ],
                default="Onbekend",
                max_length=200,
            ),
        ),
    ]
