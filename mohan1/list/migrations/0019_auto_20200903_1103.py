# Generated by Django 3.0.8 on 2020-09-03 05:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0018_auto_20200903_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='save_order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 3, 5, 33, 10, 814838, tzinfo=utc)),
        ),
    ]
