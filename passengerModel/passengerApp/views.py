from django.shortcuts import render
from passengerApp.models import Passenger

# Create your views here.
def passengerdata(request):
    passenger = Passenger.objects.all()
    passengerDict = {'passenger':passenger}
    return render(request,'passengerApp/passanger.html',passengerDict)