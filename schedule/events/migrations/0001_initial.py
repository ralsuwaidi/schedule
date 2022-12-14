# Generated by Django 4.0.8 on 2022-11-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(help_text='If you are not an organization please leave this field blank', max_length=100, verbose_name='Organization name')),
                ('private', models.BooleanField(default=False, help_text='Private events will be hidden from the public.', verbose_name='Is your event private?')),
                ('poc_name', models.CharField(help_text='Name of the person we should contact', max_length=100, verbose_name='POC Name')),
                ('email', models.EmailField(help_text='Email of the person we should contact', max_length=254, verbose_name='Email')),
                ('event_name', models.CharField(help_text='The name of the event will appear in eventbrite', max_length=100, verbose_name='Event Name')),
                ('event_start', models.DateTimeField(help_text='mm/dd/yyyy')),
                ('event_end', models.DateTimeField(help_text='mm/dd/yyyy')),
                ('description', models.TextField(blank=True, help_text='Please describe the event with as much detail as possible', null=True)),
                ('event_type', models.CharField(choices=[('OF', 'Offline'), ('OL', 'Online'), ('HY', 'Hybrid')], help_text='How will this event be hosted?', max_length=2, verbose_name='Event Type')),
                ('audience', models.CharField(choices=[('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')], help_text='Which audience level is this event geared for?', max_length=2, verbose_name='Audience Level')),
                ('website', models.URLField(blank=True, help_text='Does your event have a website?', null=True, verbose_name='Event Website')),
                ('file', models.FileField(blank=True, help_text='Please attach any file that is related to the event', null=True, upload_to='files', verbose_name='Event file')),
                ('comments', models.TextField(blank=True, help_text='Any additional comments?', null=True)),
            ],
        ),
    ]
