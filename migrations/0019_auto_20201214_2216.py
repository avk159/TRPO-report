# Generated by Django 3.1.3 on 2020-12-14 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0018_auto_20201214_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 22, 16, 13, 149753)),
        ),
        migrations.AlterField(
            model_name='person',
            name='crypt',
            field=models.CharField(default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 22, 16, 13, 148790)),
        ),
    ]