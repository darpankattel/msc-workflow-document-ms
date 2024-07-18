# Generated by Django 2.1.7 on 2023-08-16 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0007_coordinator_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='programName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programCoordinator', to='college.Programme'),
        ),
    ]
