# Generated by Django 2.1.1 on 2018-11-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-id'], 'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterField(
            model_name='status',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
