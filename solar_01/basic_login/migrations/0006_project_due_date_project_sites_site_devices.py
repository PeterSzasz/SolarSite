# Generated by Django 4.1 on 2022-08-28 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_login', '0005_alter_properties_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='project',
            name='sites',
            field=models.ManyToManyField(related_name='site', to='basic_login.site'),
        ),
        migrations.AddField(
            model_name='site',
            name='devices',
            field=models.ManyToManyField(related_name='device', to='basic_login.device'),
        ),
    ]
