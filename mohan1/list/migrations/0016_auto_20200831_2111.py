# Generated by Django 3.0.8 on 2020-08-31 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0015_auto_20200831_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='save_order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='save_order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 31, 15, 41, 16, 921488, tzinfo=utc)),
        ),
    ]
