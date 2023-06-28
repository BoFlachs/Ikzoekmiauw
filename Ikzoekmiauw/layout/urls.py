from django.urls import path
from . import views

urlpatterns = [
    # Linke to the homepage
    path("", views.home, name="home"),
    path("privacy/", views.privacy, name="privacy"),
    path("ditjes-en-datjes/", views.ditjes, name="ditjesEnKatjes"),
]
