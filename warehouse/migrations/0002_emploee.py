# Generated by Django 2.1.3 on 2018-11-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emploee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=20)),
                ('emppassword', models.CharField(max_length=30)),
                ('emporder', models.IntegerField()),
                ('empposit', models.CharField(max_length=20)),
                ('empphone', models.CharField(max_length=20)),
            ],
        ),
    ]