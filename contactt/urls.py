from django.urls import path

from . import views

urlpatterns = [
    path('contact',views.contactt, name="contactt")
    ]