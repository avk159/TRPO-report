# Generated by Django 3.1.3 on 2022-04-27 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0094_auto_20220427_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 18, 41, 32, 88643)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 18, 41, 32, 88643)),
        ),
    ]
