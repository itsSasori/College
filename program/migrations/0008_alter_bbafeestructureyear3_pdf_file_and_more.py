# Generated by Django 5.0.2 on 2024-02-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_delete_coursepdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbafeestructureyear3',
            name='pdf_file',
            field=models.ImageField(blank=True, null=True, upload_to='pdf_files/'),
        ),
        migrations.AlterField(
            model_name='bbafeestructureyear4',
            name='pdf_file',
            field=models.ImageField(blank=True, null=True, upload_to='pdf_files/'),
        ),
    ]