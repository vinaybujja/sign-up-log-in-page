# Generated by Django 4.2 on 2023-05-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0006_registration_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
    ]