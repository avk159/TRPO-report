# Generated by Django 3.1.3 on 2022-03-04 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0021_auto_20220303_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 11, 16, 33, 606584)),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 11, 16, 33, 606584)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 11, 16, 33, 606584)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 11, 16, 33, 606584)),
        ),
    ]
