# Generated by Django 2.2 on 2022-12-03 23:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2022, 12, 3, 18, 19, 5, 166109))),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('score_question', models.IntegerField(default=0, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Tests')),
            ],
        ),
        migrations.CreateModel(
            name='IntentoTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score_total', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime(2022, 12, 3, 18, 19, 5, 166109))),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Tests')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='AnswersValidate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Questions')),
            ],
        ),
    ]
