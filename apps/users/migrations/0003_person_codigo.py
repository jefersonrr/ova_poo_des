# Generated by Django 2.2 on 2022-12-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221203_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='codigo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
