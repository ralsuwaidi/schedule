# Generated by Django 4.0.8 on 2022-11-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_eventmodel_is_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='phone',
            field=models.CharField(default=555555, max_length=50, verbose_name='Phone number'),
            preserve_default=False,
        ),
    ]
