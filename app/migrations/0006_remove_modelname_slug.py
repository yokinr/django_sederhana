# Generated by Django 4.1.3 on 2022-12-30 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_modelname_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelname',
            name='slug',
        ),
    ]
