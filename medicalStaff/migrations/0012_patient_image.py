# Generated by Django 3.0.5 on 2020-05-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalStaff', '0011_anesthesiste'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
