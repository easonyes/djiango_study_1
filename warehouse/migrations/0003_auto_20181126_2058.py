# Generated by Django 2.1.3 on 2018-11-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_present_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='present',
            name='off_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True),
        ),
    ]