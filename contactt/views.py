from django.shortcuts import render, redirect
from .models import contact2
# Create your views here.
def contactt(request):
  if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact_no = request.POST["contact_no"]
        message = request.POST["message"]

        contact = contact2(name=name, email=email, contact_no = contact_no, message=message)
        contact.save();
        print("contact created")
        return redirect('/')
    
  else:
        return render(request, "contact.html")

