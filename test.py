from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from datetime import datetime

from gcsa.attachment import Attachment

from beautiful_date import Jan, Apr, Nov


calendar = GoogleCalendar('e0e86510c60950ccb90b85667fafa7c23bbffbe7cd6b361a9f80320d09eca1d0@group.calendar.google.com', credentials_path='./.credentials/credentials.json', token_path='./.credentials/token.pickle')


# yellow color event
color_id = '4'
event = Event(
        'TBC',
        start=datetime.now(),
        end=datetime.now(),
        color_id='2'
    ) 
event = calendar.add_event(event)
print(event.event_id)
