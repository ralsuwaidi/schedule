from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Row, Column
from .models import PermitModel
from django.forms import ModelForm

class OrganizationForm(forms.Form):
    organization = forms.CharField(label="Organization name", help_text="If you are not an organization please leave this field blank" ,max_length=100)
    private = forms.BooleanField(label="Is your event private?",help_text="Private events will be hidden from the public.", required=False )

    def __init__(self, *args, **kwargs):
        super(OrganizationForm, self).__init__(*args, **kwargs)
        self.fields['private'].widget.attrs['class'] = 'h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'


class POCForm(forms.Form):
    poc_name = forms.CharField(help_text="Name of the person we should contact", max_length=100)
    email = forms.EmailField(help_text="Email of the person we should contact")


class EventForm(forms.Form):
    TYPE_CHOICES = (
        ('OF', 'Offline'),
        ('OL', 'Online'),
        ('HY', 'Hybrid'),
    )

    AUDIENCE_CHOICE = (
        ('BE', 'Beginner'),
        ('IN', 'Intermediate'),
        ('AD', 'Advanced'),
    )

    SEATING_CHOICE = (
        ('TH', 'Theatre'),
        ('CL', 'Classroom'),
        ('BO', 'Boardroom'),
        ('CA', 'Cabaret'),
        ('UT', 'U-Shaped (With Tables)'),
        ('UW', 'U-Shaped (Without Tables)'),
    )

    event_name = forms.CharField(label="Event Name", help_text="The name of the event will appear in eventbrite", max_length=100)
    event_start = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}), help_text='mm/dd/yyyy')
    event_end = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}), help_text='mm/dd/yyyy')
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), help_text="Please describe the event with as much detail as possible", required=False)
    event_type = forms.ChoiceField(choices=TYPE_CHOICES, label='Event Type', help_text='How will this event be hosted?')
    audience = forms.ChoiceField(choices=AUDIENCE_CHOICE, label='Audience Level', help_text='Which audience level is this event geared for?')
    website = forms.URLField(label="Event Website", help_text="Does your event have a website?", required=False)
    file = forms.FileField(label="Event file", help_text="Please attach any file that is related to the event", required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), help_text="Any additional comments?", required=False)
    attendees = forms.IntegerField(label="Number of Attendees", help_text="Number of expected attendees if the event is private", required=False, initial=0)
    seating = forms.ChoiceField(choices=SEATING_CHOICE, label='Seating arrangement', help_text='What style of seating are you looking for?')
    

class PermitForm(ModelForm):
    class Meta:
        model = PermitModel
        fields = [
            'has_catering',
            'catering',
            'has_photography',
            'photography',
            'photography_number',
            'equipment',
            'has_external_setup',
            'setup_details',
            'setup_datetime',
        ]