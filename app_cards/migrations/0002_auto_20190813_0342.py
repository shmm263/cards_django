# Generated by Django 2.2.4 on 2019-08-13 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medexamination',
            name='dat_end',
            field=models.DateField(default=datetime.datetime(2021, 8, 13, 3, 42, 49, 744695), verbose_name='Дата действия справки'),
        ),
    ]
