from django.db import models

# Create your models here.
class Kat(models.Model):
    naam = models.CharField(max_length=200)
    
    MAN = "Man"
    VROUW = "Vrouw"
    ONBEKEND = "Onbekend"
    GESLACHT_CHOICES = [
        (MAN, "Mannelijk"),
        (VROUW, "Vrouwelijk"),
        (ONBEKEND, "Onbekend"),
    ]
    geslacht = models.CharField(max_length=200, 
                                choices=GESLACHT_CHOICES,
                                default=ONBEKEND)    
    foto = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    
    def __str__(self):
        return self.naam