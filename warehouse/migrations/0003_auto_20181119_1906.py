# Generated by Django 2.1.3 on 2018-11-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_emploee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emploee',
            name='empname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='emploee',
            name='emporder',
            field=models.IntegerField(choices=[(0, '普通员工'), (1, '主管'), (2, 'BOSS')], default=0),
        ),
        migrations.AlterField(
            model_name='emploee',
            name='emppassword',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='emploee',
            name='empphone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='emploee',
            name='empposit',
            field=models.CharField(max_length=200),
        ),
    ]