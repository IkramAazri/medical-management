# Generated by Django 3.0.5 on 2020-05-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalStaff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
