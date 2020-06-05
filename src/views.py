from django.shortcuts import render 
from .models import Event,Upcoming_Event
from django.http import JsonResponse


# Create your views here.
def index(request):
    all_events = list(Event.objects.values())
    return render(request, 'index.html', {'body': True, 'all_events': all_events})

def about(request):
    return render(request, 'index.html', {'about': True})

def members(request):
    return render(request, 'index.html', {'members': True})

def events(request):
    all_events = list(Event.objects.values())
    return render(request, 'index.html', {'events': True, 'all_events': all_events})

def read_more(request):
    return render(request, 'index.html', {'read_more': True})

def read_event(request,id):
    all_events = list(Event.objects.values())
    event = list(Event.objects.values())[id-1]
    return render(request, 'index.html', {'read_event':True, 'event': event, 'all_events': all_events})

def volunter(request):
    all_volunter_events = list(Upcoming_Event.objects.values())
    return render(request, 'index.html', {'volunter':True, 'all_events':all_volunter_events})

def read_volunter_event(request,id):
    all_volunter_events = list(Upcoming_Event.objects.values())
    event = list(Upcoming_Event.objects.values())[id-1]
    return render(request, 'index.html', {'read_event_vol':True, 'event': event, 'all_events': all_volunter_events})
