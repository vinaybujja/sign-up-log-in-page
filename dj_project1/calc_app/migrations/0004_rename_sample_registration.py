# Generated by Django 4.2 on 2023-05-14 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0003_rename_lastname_sample_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sample',
            new_name='registration',
        ),
    ]
