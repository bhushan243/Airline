# Generated by Django 3.0.3 on 2021-04-26 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0004_auto_20210419_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='city',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='country',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='state',
        ),
    ]