from django.shortcuts import render
from .models import apartments
import threading
# Create your views here.



def index(request):
    dest=apartments.objects.all()

   
    return render(request, "index.html", {'destt' : dest})




