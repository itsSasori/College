# Generated by Django 5.0.2 on 2024-02-14 07:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_coursepdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepdf',
            name='name',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
    ]
