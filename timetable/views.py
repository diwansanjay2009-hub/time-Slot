

# Create your views here.
from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):
    # Retrieve all timetable records, ordered chronologically by day and start time
    slots = TimeSlot.objects.all().order_by('day', 'start_time')
    return render(request, 'timetable.html', {'slots': slots})
