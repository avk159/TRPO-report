# Generated by Django 3.1.3 on 2022-04-25 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0056_auto_20220425_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoint',
            name='approved',
        ),
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 6, 11, 530880)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 6, 11, 530880)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 6, 11, 530880)),
        ),
    ]
