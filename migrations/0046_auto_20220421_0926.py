# Generated by Django 3.1.3 on 2022-04-21 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0045_auto_20220421_0924'),
    ]

    operations = [
        migrations.DeleteModel(
            name='appoint',
        ),
        migrations.AlterField(
            model_name='appoint2',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 26, 50, 419721)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 26, 50, 418722)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 26, 50, 418722)),
        ),
    ]
