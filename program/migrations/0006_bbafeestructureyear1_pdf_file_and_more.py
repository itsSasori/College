# Generated by Django 5.0.2 on 2024-02-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_coursepdf_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbafeestructureyear1',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_files/'),
        ),
        migrations.AddField(
            model_name='bbafeestructureyear2',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_files/'),
        ),
        migrations.AddField(
            model_name='bbafeestructureyear3',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_files/'),
        ),
        migrations.AddField(
            model_name='bbafeestructureyear4',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_files/'),
        ),
    ]
