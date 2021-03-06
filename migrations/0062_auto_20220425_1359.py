# Generated by Django 3.1.3 on 2022-04-25 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0061_auto_20220425_1359'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appoint',
        ),
        migrations.AlterField(
            model_name='message',
            name='msgdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 59, 47, 155778)),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 25, 13, 59, 47, 155778)),
        ),
       # migrations.AddConstraint(
       #     model_name='message',
       #     constraint=models.UniqueConstraint(fields=('doctor', 'patient', 'appointdate', 'appointtime'), name='unique appointment'),
       # ),
       # migrations.AddConstraint(
       #     model_name='message',
       #     constraint=models.UniqueConstraint(fields=('doctor', 'appointdate', 'appointtime'), name='unique_appdoc'),
       # ),
       # migrations.AddConstraint(
       #     model_name='message',
       #     constraint=models.UniqueConstraint(fields=('patient', 'appointdate', 'appointtime'), name='unique_apppatient'),
       # ),
    ]
