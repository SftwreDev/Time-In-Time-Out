# Generated by Django 3.1.7 on 2021-04-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_timeintimeout_shift_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeintimeout',
            name='task',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
