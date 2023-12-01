# Generated by Django 4.2.6 on 2023-12-01 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.TextField(null=True)),
                ("text", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SiteDetail",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(default="Clothing Store", max_length=200)),
                ("desc", models.TextField(null=True)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20, null=True)),
                ("work_hours", models.CharField(max_length=500, null=True)),
                ("address", models.CharField(max_length=500, null=True)),
                (
                    "fb",
                    models.URLField(
                        default="https://www.facebook.com", verbose_name="Facebook"
                    ),
                ),
                (
                    "ig",
                    models.URLField(
                        default="https://www.instagram.com", verbose_name="Instagram"
                    ),
                ),
                (
                    "tw",
                    models.URLField(
                        default="https://www.twitter.com", verbose_name="Twitter"
                    ),
                ),
                (
                    "ln",
                    models.URLField(
                        default="https://www.linkedin.com", verbose_name="LinkeIn"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamMember",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Co-Founder", "Co-Founder"),
                            ("Product Expert", "Product Expert"),
                            ("Chief Marketing", "Chief Marketing"),
                            ("Product Specialist", "Product Specialist"),
                            ("Product Photographer", "Product Photographer"),
                            ("General Manager", "General Manager"),
                        ],
                        max_length=200,
                    ),
                ),
                ("desc", models.CharField(max_length=300)),
                ("avatar", models.ImageField(upload_to="team/")),
                (
                    "fb",
                    models.URLField(
                        default="https://www.facebook.com", verbose_name="Facebook"
                    ),
                ),
                (
                    "ig",
                    models.URLField(
                        default="https://www.instagram.com", verbose_name="Instagram"
                    ),
                ),
                (
                    "tw",
                    models.URLField(
                        default="https://www.twitter.com", verbose_name="Twitter"
                    ),
                ),
                (
                    "ln",
                    models.URLField(
                        default="https://www.linkedin.com", verbose_name="LinkeIn"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
