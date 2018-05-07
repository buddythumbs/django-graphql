# Generated by Django 2.0 on 2018-02-13 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logistics', '0001_initial'),
        ('cockpit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionplan',
            name='materials',
            field=models.ManyToManyField(blank=True, related_name='associated_cois', to='logistics.Material'),
        ),
        migrations.AddField(
            model_name='actionplan',
            name='reviewer_1st_line',
            field=models.ManyToManyField(blank=True, related_name='reviewed_action_plans_1st', to='cockpit.Engineer'),
        ),
        migrations.AddField(
            model_name='actionplan',
            name='reviewer_2nd_line',
            field=models.ManyToManyField(blank=True, related_name='reviewed_action_plans_2nd', to='cockpit.Engineer'),
        ),
        migrations.AddField(
            model_name='actionplan',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submitted_action_plans', to='cockpit.Engineer'),
        ),
        migrations.AddField(
            model_name='actionplan',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associated_action_plans', to='cockpit.Tool'),
        ),
    ]
