# Generated by Django 2.1.1 on 2018-11-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20181109_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telegram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
    ]