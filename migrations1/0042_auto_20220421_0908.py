# Generated by Django 3.1.3 on 2022-04-21 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0041_auto_20220421_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoint',
            name='apptime',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 8, 14, 444439)),
        ),
        migrations.AlterField(
            model_name='appoint2',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 8, 14, 444439)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 8, 14, 443443)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 8, 14, 443443)),
        ),
    ]