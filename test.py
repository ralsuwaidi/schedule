from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from datetime import datetime

from gcsa.attachment import Attachment

from beautiful_date import Jan, Apr, Nov


calendar = GoogleCalendar()

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
