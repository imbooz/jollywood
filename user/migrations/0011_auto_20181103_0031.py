# Generated by Django 2.1.1 on 2018-11-02 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20181102_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]