# Generated by Django 4.0.8 on 2022-11-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_eventmodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='other_seating',
            field=models.TextField(blank=True, help_text='If none of the above satisfies your requirement please detail how you would like the seating arrangements to be', null=True, verbose_name='Other Seating Arrangement'),
        ),
    ]
