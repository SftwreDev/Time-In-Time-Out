# Generated by Django 3.1.7 on 2021-04-04 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210404_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeintimeout',
            name='status',
            field=models.CharField(choices=[('Time In', 'Time In'), ('Time Out', 'Time Out'), ('Break In', 'Break In'), ('Break Out', 'Break Out')], default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]