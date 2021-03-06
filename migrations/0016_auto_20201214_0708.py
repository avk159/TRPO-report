# Generated by Django 3.1.3 on 2020-12-14 00:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0015_auto_20201211_1402'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messagestat',
        ),
        migrations.AddField(
            model_name='message',
            name='key',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='MySite.person'),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 7, 8, 37, 691224)),
        ),
        migrations.AlterField(
            model_name='person',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 7, 8, 37, 690190)),
        ),
    ]
