from django.urls import path
from eventportalapp.views import events,register,eventdetail,competition,registercompetition,competitiondetail,calendar

app_name="eventportal"


urlpatterns = [
    path('',events,name="events"),
    path("register/",register,name="register"),
    path("calendar/",calendar,name="calendar"),
    path("eventdetail/<str:title>/",eventdetail,name="eventdetail"),
    path("competition/",competition,name="competition"),
    path("registercompetition/",registercompetition,name="registercompetition"),
    path("competitiondetail/<str:title>/",competitiondetail,name="competitiondetail"),
]
