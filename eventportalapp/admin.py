from django.contrib import admin
from eventportalapp.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display=["id","title","dept","venue","date","time","desc","url","img"]

admin.site.register(Event,EventAdmin)