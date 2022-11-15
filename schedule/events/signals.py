from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import EventModel, PermitModel
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
        import requests



@receiver(post_save, sender=EventModel)
def create_event(sender, instance, created, **kwargs):
    calendar = GoogleCalendar('e0e86510c60950ccb90b85667fafa7c23bbffbe7cd6b361a9f80320d09eca1d0@group.calendar.google.com',credentials_path='./.credentials/credentials.json', token_path='./.credentials/token.pickle')
    if not created:
        if instance.is_approved:
            if not instance.private:
                title =  str(instance.id) + ' ' + instance.event_name
                event_type = dict(EventModel.TYPE_CHOICES).get(instance.event_type)
                audience = dict(EventModel.AUDIENCE_CHOICE).get(instance.audience)
                description = '<h2>' + instance.organization + '</h2>' + (instance.description or '') + '<br/><br/>' + event_type + '<br/>' + audience
                
                event = calendar.get_event(instance.gc_id)
                event.summary = title
                event.description = description
                event.color_id = '1'
                calendar.update_event(event)

                instance.is_updated = True
        
            else:
                title = str(instance.id) + ' ' + 'Private Event'
                description = 'Private event from one of our partners'

                event = calendar.get_event(instance.gc_id)
                event.summary = title
                event.description = description
                event.color_id = '2'
                calendar.update_event(event)

                instance.is_updated = True

        if instance.is_rejected:
            # TODO: send rejection email
            event = calendar.get_event(instance.gc_id)
            calendar.delete_event(event)


    else:
        # create a google event TBC
        
        # yellow color event
        color_id = '5'
        event = Event(
                'TBC - ' + str(instance.id),
                start=instance.event_start,
                end=instance.event_end,
                color_id=color_id
            ) 
        event = calendar.add_event(event)

        # dont start another instance
        post_save.disconnect(create_event, sender=EventModel)
        instance.gc_id = event.event_id
        instance.save()
        post_save.connect(create_event, sender=EventModel)

        ## send notification
        url = 'https://ntfy.sh/chq-events'
        headers = {
            "Title": "New CHQ Event Added " + str(instance.id),

        }
        data = {
            'data': 'A new event has been added. Please log into the admin panel to view and approve'
        }
        requests.post(url, json = data, headers=headers)




@receiver(pre_delete, sender=EventModel)
def delete_event(sender, instance, **kwargs):
    # delete event on model delete
    try:
        calendar = GoogleCalendar('e0e86510c60950ccb90b85667fafa7c23bbffbe7cd6b361a9f80320d09eca1d0@group.calendar.google.com',credentials_path='./.credentials/credentials.json', token_path='./.credentials/token.pickle')
        event = calendar.get_event(instance.gc_id)
        calendar.delete_event(event)
    except:
        pass