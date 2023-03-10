# Generated by Django 2.2 on 2022-12-03 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('type_document', models.CharField(max_length=20)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthdate_place', models.CharField(blank=True, max_length=300, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Person')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Rol')),
            ],
        ),
    ]
