# Generated by Django 5.0 on 2024-10-06 00:48

import django.contrib.postgres.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transport",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("lat", models.FloatField(null=True)),
                ("lon", models.FloatField(null=True)),
                ("name", models.CharField(max_length=100)),
                ("station_code", models.CharField(max_length=100)),
                (
                    "transport_type",
                    models.CharField(
                        choices=[("bus", "Bus"), ("auto", "Auto"), ("metro", "Metro")],
                        max_length=20,
                    ),
                ),
                (
                    "line",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        default=list,
                        size=None,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(null=True)),
            ],
        ),
    ]
