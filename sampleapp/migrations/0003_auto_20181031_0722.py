# Generated by Django 2.1.2 on 2018-10-31 01:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_auto_20181031_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 1, 52, 10, 235394, tzinfo=utc)),
        ),
    ]
