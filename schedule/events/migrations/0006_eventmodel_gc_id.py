# Generated by Django 4.0.8 on 2022-11-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_permitmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='gc_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Google Event Id'),
        ),
    ]
