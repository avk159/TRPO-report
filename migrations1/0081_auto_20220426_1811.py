# Generated by Django 3.1.3 on 2022-04-26 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0080_auto_20220426_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 26, 18, 11, 47, 850506)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 26, 18, 11, 47, 850506)),
        ),
    ]