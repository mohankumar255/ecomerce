# Generated by Django 3.0.8 on 2020-08-30 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20200830_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='iamge',
            new_name='image',
        ),
    ]