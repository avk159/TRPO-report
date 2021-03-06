# Generated by Django 3.1.3 on 2022-04-20 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0031_auto_20220420_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 20, 57, 54, 468421)),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='apptime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 20, 57, 54, 467389)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 20, 57, 54, 467389)),
        ),
    ]
