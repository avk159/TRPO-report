# Generated by Django 3.1.3 on 2022-04-21 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0046_auto_20220421_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint2',
            name='appointreg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 39, 40, 188939)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 39, 40, 187940)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 39, 40, 187940)),
        ),
        migrations.CreateModel(
            name='Appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=20)),
                ('patient', models.CharField(max_length=20)),
                ('appointdate', models.DateField()),
                ('appointtime', models.TimeField(default='00:00')),
                ('appointreg', models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 21, 9, 39, 40, 187940))),
            ],
            options={
                'unique_together': {('doctor', 'patient', 'appointdate', 'appointtime')},
            },
        ),
    ]