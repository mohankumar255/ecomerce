# Generated by Django 3.0.8 on 2020-08-31 09:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0014_auto_20200831_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='save_order',
            old_name='state',
            new_name='state1',
        ),
        migrations.AlterField(
            model_name='save_order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 31, 9, 54, 46, 82015, tzinfo=utc)),
        ),
    ]
