# Generated by Django 4.2.7 on 2024-02-19 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_Two', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date1',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
