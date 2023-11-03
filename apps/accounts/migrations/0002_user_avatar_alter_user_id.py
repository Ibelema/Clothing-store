# Generated by Django 4.2.6 on 2023-11-03 18:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('00136656-6d0f-4fb8-8099-253ae1169525'), primary_key=True, serialize=False, unique=True),
        ),
    ]