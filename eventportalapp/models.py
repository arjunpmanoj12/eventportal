from django.db import models
from django.core.validators import URLValidator

DEPARTMENTS = (
    ("CSE", "Computer Science and Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EEE", "Electrical and Electronics Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CE", "Civil Engineering"),
    (None, "None")
) 

class Event(models.Model):
    title = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    date = models.DateField()  
    time = models.CharField(max_length=30)
    desc = models.TextField(default=None)
    img = models.ImageField(upload_to='event_img')
    dept = models.CharField(max_length=30, choices=DEPARTMENTS, default=None)
    url = models.URLField(null=True,validators=[URLValidator()],max_length=100)

    def __str__(self):
        return self.title
