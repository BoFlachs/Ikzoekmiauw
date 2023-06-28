from django.urls import path
from . import views

urlpatterns = [
   path("", views.katalogus, name="katalogus") 
]
