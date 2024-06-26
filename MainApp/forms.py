from django.forms import ModelForm
from .models import Event

class EventRegForm(ModelForm):
    class Meta:
        model = Event
        fields = ['family_name', 'guardian_name', 'event_type',
                  'participants', 'date', 'time_category',
                  'amenities', 'strt_time', 'end_time', 'location']