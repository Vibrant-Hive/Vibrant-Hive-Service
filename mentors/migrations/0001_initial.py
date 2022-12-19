# Generated by Django 4.1.4 on 2022-12-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("active", models.BooleanField()),
                ("availability", models.CharField(max_length=100)),
                ("designation", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("experience", models.IntegerField(default=0)),
                ("full_name", models.CharField(max_length=100)),
                ("languages", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=20)),
                ("rate", models.IntegerField(default=0)),
                ("resume", models.TextField()),
                ("role", models.CharField(max_length=200)),
                ("skills", models.CharField(max_length=200)),
            ],
        ),
    ]