from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Event, Amenity
from .forms import EventRegForm

def home(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "home.html", context)

def add(request):
    form = EventRegForm()
    amenities = Amenity.objects.all()

    if request.method == "POST":
        form = EventRegForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Event added successfully!')

    context = {"form": form, "amenities": amenities}

    return render(request, "add.html", context)

def view_edit(request, event_pk):
    form = EventRegForm()
    evt_obj = Event.objects.get(pk=event_pk)

    if request.method == 'POST' and ('save_button' in request.POST):
        form = EventRegForm(request.POST, instance=evt_obj)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Event saved successfully!')
            return redirect('homepage')
    elif request.method == 'POST' and ('delete_button' in request.POST):
        evt_obj.delete()
        messages.add_message(request, messages.SUCCESS, 'Event deleted successfully')
        return redirect('homepage')

    amenities = Amenity.objects.all()

    evt_obj.date = str(evt_obj.date)
    evt_obj.strt_time = str(evt_obj.strt_time)
    evt_obj.end_time = str(evt_obj.end_time)
    
    context = {"event": evt_obj, "amenities": amenities, "form": form}
    return render(request, "view-edit.html", context)