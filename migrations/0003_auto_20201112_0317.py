# Generated by Django 3.1.3 on 2020-11-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0002_mesagges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesagge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mfrom', models.CharField(max_length=20)),
                ('mto', models.CharField(max_length=20)),
                ('mcontent', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Mesagges',
        ),
    ]
