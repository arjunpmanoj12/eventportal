from django.urls import path
from eventportalapp.views import eventdetail, events,register

app_name="eventportal"


urlpatterns = [
    path('',events),
    path("registered/",register,name="register"),
    path("eventdetail/<str:title>/",eventdetail,name="eventdetail")
    
]
