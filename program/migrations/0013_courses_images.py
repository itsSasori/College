# Generated by Django 5.0.2 on 2024-02-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0012_courses_totalyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
