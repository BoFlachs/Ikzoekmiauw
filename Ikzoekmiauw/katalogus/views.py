from django.shortcuts import render
from .models import Kat, Kattensoort
from rest_framework import generics
from django.core import serializers as ser
from django_filters.views import FilterView
from . import serializers
from . import filters

# Create your views here.
class KattenListView(FilterView):
    model = Kat
    template_name = "katalogus.html"
    # paginate_by = 6
    filterset_class = filters.KatFilter
    ordering_fields = ['soort']
    
# def katalogus(request):
#     katten = Kat.objects.all()
#     katten_json = ser.serialize('json', katten)
#     return render(request, 'katalogus.html', {"katten": katten_json})

class KattenView(generics.ListCreateAPIView):
    ordering_fields = ['naam']
    queryset = Kat.objects.all()
    serializer_class = serializers.KatSerializer
    
def kat(request, pk):
    kat = Kat.objects.get(pk=pk)
    return render(request, 'kat.html', {'kat': kat})
        
    
class SingleKatView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kat.objects.all()
    serializer_class = serializers.KatSerializer

class KattenSoortView(generics.ListCreateAPIView):
    ordering_fields = ['soort']
    queryset = Kattensoort.objects.all()
    serializer_class = serializers.KattenSoortSerializer