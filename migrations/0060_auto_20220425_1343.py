# Generated by Django 3.1.3 on 2022-04-25 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0059_auto_20220425_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoint',
            name='approved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 43, 54, 363347)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 43, 54, 363347)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 43, 54, 363347)),
        ),
    ]
