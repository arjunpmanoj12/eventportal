import json

from django.shortcuts import render, get_object_or_404,redirect
from django.http.response import HttpResponse

from .models import Event


def eventdetail(request, title):
    obj = get_object_or_404(Event, title=title)
    return render(request, "eventdetail.html", {'event': obj})


def register(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        venue = request.POST.get("venue")
        date = request.POST.get("date")
        dept = request.POST.get("dept")
        img = request.FILES.get("img")
        url = request.POST.get("url")
        time = request.POST.get("time")
        desc = request.POST.get("desc")

        Event.objects.create(
            title=title,
            venue=venue,
            date=date,
            dept=dept,
            desc=desc,
            img=img,
            url=url,
            time=time,
        )
        return redirect("/")
    else:
        return render(request, "register.html")


def events(request):
    events_list = Event.objects.all()
    context = {
        "events_lists": events_list,
    }
    return render(request, "index.html", context=context)
