# Generated by Django 4.2.6 on 2023-11-07 22:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('da980e9e-bff7-4de8-84f7-fee605d08577'), primary_key=True, serialize=False, unique=True),
        ),
    ]