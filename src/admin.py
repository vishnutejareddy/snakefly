from django.contrib import admin

# Register your models here.
from .models import Event,Upcoming_Event

admin.site.register(Event)
admin.site.register(Upcoming_Event)