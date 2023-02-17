from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "flights": Flight.objects.all()
    })
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flight.html", {
        "flight": flight,
    })