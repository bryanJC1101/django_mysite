# Generated by Django 3.0.2 on 2020-01-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeCode', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('birthDate', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
    ]
