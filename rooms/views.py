from django.shortcuts import render
from . import models

# Create your views here.
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "room/home.html", context={"all_rooms": all_rooms})
