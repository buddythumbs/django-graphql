# Generated by Django 2.0 on 2018-05-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0007_auto_20180526_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicenotification',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='service_notification', to='cockpit.Task'),
        ),
    ]
