# Generated by Django 3.0.2 on 2020-02-11 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 0, 47, 21, 596176)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 0, 47, 21, 595915)),
        ),
    ]
