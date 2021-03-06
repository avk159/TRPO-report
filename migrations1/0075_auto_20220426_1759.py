# Generated by Django 3.1.3 on 2022-04-26 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0074_auto_20220426_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 26, 17, 59, 24, 365376)),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 26, 17, 59, 24, 365376)),
        ),
    ]
