# Generated by Django 3.0.8 on 2020-08-31 05:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_auto_20200831_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save_order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 31, 5, 26, 51, 835980, tzinfo=utc)),
        ),
    ]