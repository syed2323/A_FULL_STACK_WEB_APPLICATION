from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from contactt.models import contact2
from sm.models import apartments
# Create your models here.
def login(request):
  
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            movie=contact2.objects.all()
            
            auth.login(request, user)
     
            return render(request,'index 2.html', {'moviee' : movie})
    else:
        return render(request,'login.html')
