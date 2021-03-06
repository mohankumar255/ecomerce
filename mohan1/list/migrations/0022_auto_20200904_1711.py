# Generated by Django 3.0.8 on 2020-09-04 11:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0021_auto_20200903_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, default=0, upload_to='pics/%y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='save_order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 11, 41, 10, 312154, tzinfo=utc)),
        ),
    ]
