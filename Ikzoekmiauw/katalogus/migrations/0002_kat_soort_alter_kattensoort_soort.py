# Generated by Django 4.2.2 on 2023-06-29 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("katalogus", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="kat",
            name="soort",
            field=models.ForeignKey(
                default="Overig",
                on_delete=django.db.models.deletion.PROTECT,
                to="katalogus.kattensoort",
                to_field="soort",
            ),
        ),
        migrations.AlterField(
            model_name="kattensoort",
            name="soort",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
