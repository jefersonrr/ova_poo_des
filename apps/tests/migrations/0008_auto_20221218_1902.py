# Generated by Django 2.2 on 2022-12-18 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_auto_20221218_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intentotest',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 18, 19, 1, 58, 782532)),
        ),
        migrations.AlterField(
            model_name='intentotest',
            name='score_total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tests',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 19, 1, 58, 781497)),
        ),
    ]
