# Generated by Django 4.1 on 2022-11-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="continent_factor",
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
                ("대륙", models.CharField(max_length=1000)),
                ("factor", models.CharField(max_length=1000)),
                ("death_per_100000", models.CharField(max_length=1000)),
            ],
        ),
    ]
