# Generated by Django 4.0.1 on 2022-01-17 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
    ]