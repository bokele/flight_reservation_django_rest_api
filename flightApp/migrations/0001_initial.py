# Generated by Django 4.1.2 on 2022-10-18 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
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
                ("flifhtNumber", models.CharField(max_length=10)),
                ("operationAirlines", models.CharField(max_length=100)),
                ("departtureCity", models.CharField(max_length=100)),
                ("arrialCity", models.CharField(max_length=100)),
                ("dateOfDeparture", models.DateField()),
                ("estimatedTimeOfDeparture", models.TimeField()),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Passanger",
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
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("middleName", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "flight",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flightApp.flight",
                    ),
                ),
                (
                    "passanger",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flightApp.passanger",
                    ),
                ),
            ],
        ),
    ]