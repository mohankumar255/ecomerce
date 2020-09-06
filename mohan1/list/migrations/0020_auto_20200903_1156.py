# Generated by Django 3.0.8 on 2020-09-03 06:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0019_auto_20200903_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='save_order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 3, 6, 26, 14, 12606, tzinfo=utc)),
        ),
    ]