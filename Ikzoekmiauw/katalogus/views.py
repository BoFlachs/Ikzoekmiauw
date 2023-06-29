from django.shortcuts import render
from .models import Kat, Kattensoort
from rest_framework import generics
from . import serializers

# Create your views here.
def katalogus(request):
    return render(request, 'katalogus.html')

class KattenView(generics.ListCreateAPIView):
    ordering_fields = ['naam']
    queryset = Kat.objects.all()
    serializer_class = serializers.KatSerializer

class KattenSoortView(generics.ListCreateAPIView):
    ordering_fields = ['soort']
    queryset = Kattensoort.objects.all()
    serializer_class = serializers.KattenSoortSerializer