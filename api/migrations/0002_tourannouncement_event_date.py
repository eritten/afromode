# Generated by Django 5.2.1 on 2025-05-26 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourannouncement',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2025, 5, 26, 9, 36, 52, 504516)),
            preserve_default=False,
        ),
    ]
