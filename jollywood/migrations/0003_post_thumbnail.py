# Generated by Django 2.1.1 on 2018-10-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jollywood', '0002_auto_20181028_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='img/default_thumb.jpg', upload_to='post_thumbs'),
        ),
    ]
