# Generated by Django 3.2 on 2023-07-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalogus', '0007_kat_gecastreerd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kat',
            name='beschrijving',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
