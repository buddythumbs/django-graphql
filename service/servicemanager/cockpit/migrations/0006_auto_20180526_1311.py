# Generated by Django 2.0 on 2018-05-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0005_auto_20180526_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competency',
            name='description',
            field=models.CharField(default='FSE', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='engineer',
            name='competencies',
            field=models.ManyToManyField(blank=True, related_name='capable_engineers', to='cockpit.Competency'),
        ),
    ]
