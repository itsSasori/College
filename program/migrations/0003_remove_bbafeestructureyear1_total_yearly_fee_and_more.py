# Generated by Django 5.0.2 on 2024-02-14 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_bbafeestructureyear1_bbafeestructureyear2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbafeestructureyear1',
            name='Total_Yearly_Fee',
        ),
        migrations.RemoveField(
            model_name='bbafeestructureyear2',
            name='Total_Yearly_Fee',
        ),
        migrations.RemoveField(
            model_name='bbafeestructureyear3',
            name='Total_Yearly_Fee',
        ),
        migrations.RemoveField(
            model_name='bbafeestructureyear4',
            name='Total_Yearly_Fee',
        ),
    ]