from django.urls import path
from . import views

urlpatterns = [
   path("", views.KattenListView.as_view(), name='katalogus'),
#    path("", views.katalogus, name="katalogus"),
   path("api/katten", views.KattenView.as_view()),
   path("api/soort", views.KattenSoortView.as_view()),
   path("api/katten/<int:pk>", views.SingleKatView.as_view()),
]
