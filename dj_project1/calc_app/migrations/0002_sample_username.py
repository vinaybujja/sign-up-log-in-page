# Generated by Django 4.2 on 2023-05-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='username',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
