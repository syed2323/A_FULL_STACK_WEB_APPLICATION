from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "about.html")
def ahad(request):
    return render(request, "ahad.html")