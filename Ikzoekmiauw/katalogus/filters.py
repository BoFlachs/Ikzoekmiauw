import django_filters
from . import models
        
class KatFilter(django_filters.FilterSet):
    class Meta:
        model = models.Kat
        fields = [
                    'soort', 
                    'geslacht', 
                    'kanBijKinderen']