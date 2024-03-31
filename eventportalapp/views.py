from django.shortcuts import render,get_object_or_404,redirect

from .models import Event,Competition


def register(request):
    if request.method == "POST":
        title = request.POST.get("title")
        venue = request.POST.get("venue")
        date = request.POST.get("date")
        dept = request.POST.get("dept")
        img = request.FILES.get("img")
        url = request.POST.get("url")
        time = request.POST.get("time")
        desc = request.POST.get("desc")
    
        Event.objects.create(
            title = title,
            venue = venue,
            date = date,
            dept = dept, 
            desc =desc,
            img = img,
            url =url,
            time = time,
        )
        return redirect("/")
    else:
        return render(request,"register.html",)


def registercompetition(request):
    if request.method == "POST":
        title = request.POST.get("title")
        venue = request.POST.get("venue")
        date = request.POST.get("date")
        dept = request.POST.get("dept")
        img = request.FILES.get("img")
        url = request.POST.get("url")
        time = request.POST.get("time")
        desc = request.POST.get("desc")
    
        Competition.objects.create(
            title = title,
            venue = venue,
            date = date,
            dept = dept, 
            desc =desc,
            img = img,
            url =url,
            time = time,
        )
        return redirect("/")
    else:
        return render(request,"registercompetition.html",)
    

def competition(request):
    competition_list = Competition.objects.all()
    context = {
        "competition_lists": competition_list,
    }
    return render(request,"competitions.html",context=context)

    
def competitiondetail(request,title):
     obj = get_object_or_404(Competition ,title=title)
     return render(request,"competitiondetails.html",{'competition': obj})

    
def eventdetail(request,title):
     obj = get_object_or_404(Event ,title=title)
     return render(request,"eventdetail.html",{'event': obj})


def events(request):
    events_list = Event.objects.all()
    context = {
        "events_lists": events_list,
    }
    return render(request, "index.html", context=context)


def calendar(request):
    return render(request, "calendar.html")

