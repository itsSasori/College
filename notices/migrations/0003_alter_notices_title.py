# Generated by Django 5.0.2 on 2024-02-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_news_notices_created_notices_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='title',
            field=models.CharField(max_length=1024),
        ),
    ]