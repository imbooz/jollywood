# Generated by Django 2.1.1 on 2018-11-02 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profile_cropping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cropping',
        ),
    ]
