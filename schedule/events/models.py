from django.db import models
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
import os

# Create your models here.
class EventModel(models.Model):
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

    organization = models.CharField("Organization name", help_text="If you are not an organization please leave this field blank", max_length=100)
    private = models.BooleanField("Is your event private?",help_text="Private events will be hidden from the public.", default=False )
    
    poc_name = models.CharField("POC Name", help_text="Name of the person we should contact", max_length=100)
    email = models.EmailField("Email", help_text="Email of the person we should contact")

    event_name = models.CharField("Event Name", help_text="The name of the event will appear in eventbrite", max_length=100)
    event_start = models.DateTimeField(help_text='mm/dd/yyyy')
    event_end = models.DateTimeField(help_text='mm/dd/yyyy')
    description = models.TextField(help_text="Please describe the event with as much detail as possible", blank=True, null=True)
    event_type = models.CharField('Event Type', choices=TYPE_CHOICES, help_text='How will this event be hosted?', max_length=2)
    audience = models.CharField('Audience Level', choices=AUDIENCE_CHOICE,  help_text='Which audience level is this event geared for?', max_length=2)
    website = models.URLField("Event Website", help_text="Does your event have a website?", blank=True, null=True)
    file = models.FileField("Event file", help_text="Please attach any file that is related to the event", blank=True, null=True, upload_to='files')
    comments = models.TextField(help_text="Any additional comments?", blank=True, null=True)

    attendees = models.IntegerField("Number of Attendees", help_text="Number of expected attendees if the event is private", default=0, null=True, blank=True)
    seating = models.CharField('Seating arrangement', choices=SEATING_CHOICE, help_text='What style of seating are you looking for?', default='TH', max_length=2)
    
    # to save to google calendar and change event details
    gc_id = models.CharField("Google Event Id", blank=True, null=True, max_length=50)

    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name


    def save(self, *args, **kwargs):
        if self.gc_id == None:
            # create a google event TBC
            print(os.getcwd())
            calendar = GoogleCalendar(credentials_path='./.credentials/credentials.json', token_path='./.credentials/token.pickle')

            
            # yellow color event
            color_id = '5'
            event = Event(
                    'TBC',
                    start=self.event_start,
                    end=self.event_end,
                    color_id=color_id
                ) 
            event = calendar.add_event(event)
            self.gc_id = event.event_id

        super(EventModel, self).save(*args, **kwargs)



class PermitModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    has_catering = models.BooleanField("Request Catering Permit", help_text="Are you bringing your own catering company?", default=False)
    catering = models.CharField("Catering Company Name", max_length=100, null=True, blank=True)
    has_photography = models.BooleanField("Request Photography Permit", help_text="Are you bringing your own photographer/videographer?", default=False)
    photography = models.CharField("Photography Company Name", help_text="If the photographer is freelance please type 'Freelance'", max_length=100, null=True, blank=True)
    photography_number = models.IntegerField("Number of photographers", default=0)
    equipment = models.TextField(help_text="Photography equipment details", blank=True, null=True)
    has_external_setup = models.BooleanField("Request External Setup Permit", help_text="Are you bringing your own external setup (chairs, tables, etc)?", default=False)
    setup_details = models.TextField(help_text="External setup details (tables, chairs, etc)", blank=True, null=True)
    setup_datetime = models.DateTimeField("External Setup Arrival", help_text="External setup date and time", blank=True, null=True)