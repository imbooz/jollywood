# Generated by Django 2.1.1 on 2018-11-09 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
