# Generated by Django 2.1.1 on 2018-11-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jollywood', '0013_books_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Elementary', 'Elementary'), ('Pre', 'Pre-Intermediate'), ('Intermediate', 'Intermediate'), ('Upper', 'Upper-Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=20),
        ),
    ]
