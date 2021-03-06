# Generated by Django 2.1.1 on 2018-11-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20181102_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(choices=[('English', 'English'), ('Russian', 'Russian'), ('Mathematics', 'Mathematics')], default='English', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Elementary', 'Elementary'), ('Pre-Intermediate', 'Pre-Intermediate'), ('Intermediate', 'Intermediate'), ('Upper-Intermediate', 'Upper-Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], default='Student', max_length=20),
        ),
    ]
