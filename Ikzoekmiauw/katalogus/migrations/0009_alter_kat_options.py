# Generated by Django 3.2 on 2023-07-18 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalogus', '0008_alter_kat_beschrijving'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kat',
            options={'ordering': ['id']},
        ),
    ]
