# Generated by Django 3.0.8 on 2020-08-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50)),
                ('rate', models.IntegerField(max_length=50)),
                ('iamge', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types1', models.CharField(max_length=100)),
            ],
        ),
    ]
