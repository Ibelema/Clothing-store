# Generated by Django 4.2.6 on 2023-11-07 22:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('20348857-9ce7-45d6-be81-d08f932cc4f9'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('20348857-9ce7-45d6-be81-d08f932cc4f9'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('20348857-9ce7-45d6-be81-d08f932cc4f9'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
