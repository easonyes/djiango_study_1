# Generated by Django 2.1.3 on 2018-12-03 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20181203_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='present',
            old_name='pdepot',
            new_name='item',
        ),
    ]