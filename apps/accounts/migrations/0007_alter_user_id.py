# Generated by Django 4.2.6 on 2023-11-16 08:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6fce3746-8226-43a9-a8cd-55b3d31ef58a'), primary_key=True, serialize=False, unique=True),
        ),
    ]
