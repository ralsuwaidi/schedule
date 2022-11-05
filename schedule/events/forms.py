from django import forms

class EventForm(forms.Form):
    organization = forms.CharField(max_length=100)
    event_name = forms.CharField(max_length=100)