from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EventModel, PermitModel
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar

@receiver(post_save, sender=EventModel)
def create_event(sender, instance, created, **kwargs):
    if not created:
        calendar = GoogleCalendar(credentials_path='./.credentials/credentials.json', token_path='./.credentials/token.pickle')
        if not instance.private:
            if instance.is_approved:
                title = instance.event_name
                event_type = dict(EventModel.TYPE_CHOICES).get(instance.event_type)
                audience = dict(EventModel.AUDIENCE_CHOICE).get(instance.audience)
                description = '<h2>' + instance.organization + '</h2>' + (instance.description or '') + '<br/><br/>' + event_type + '<br/>' + audience
                
                event = calendar.get_event(instance.gc_id)
                event.summary = title
                event.description = description
                event.color_id = '1'
                calendar.update_event(event)

                instance.is_updated = True
