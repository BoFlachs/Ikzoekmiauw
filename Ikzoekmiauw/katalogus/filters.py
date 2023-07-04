import django_filters
from django import forms 

from . import models
        
class KatFilter(django_filters.FilterSet):  
    class Meta:
        model = models.Kat
        fields = [
                    'soort', 
                    'geslacht', 
                    'leeftijd',
                    'kanBijKinderen',
                    'kanBijHonden',
                    'kanBijKatten',
                    'moetNaarBuiten',
                    'specialeZorg',
                    'locatie',
                    'beschikbaarVanaf',
                    ]