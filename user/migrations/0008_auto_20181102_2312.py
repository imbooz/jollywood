# Generated by Django 2.1.1 on 2018-11-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20181102_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], default='Student', max_length=1),
        ),
    ]
