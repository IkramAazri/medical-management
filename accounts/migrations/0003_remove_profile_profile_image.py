# Generated by Django 3.0.5 on 2020-05-01 17:12

from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_profile_image'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]
