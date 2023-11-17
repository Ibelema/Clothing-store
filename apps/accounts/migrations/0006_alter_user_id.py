# Generated by Django 4.2.6 on 2023-11-07 23:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('95451d44-611d-4e90-b689-9516a44f2bec'), primary_key=True, serialize=False, unique=True),
        ),
    ]