from django.db import models
import datetime

# Create your models here.
class Kattensoort(models.Model):
    soort = models.CharField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return self.soort


class Kat(models.Model):
    # Name of the cat
    naam = models.CharField(max_length=200)
    
    # Type of cat (as a foreign key)
    soort = models.ForeignKey(Kattensoort, on_delete=models.PROTECT, 
                               to_field="soort", default="Overig")
    
    # Several choices for the sex of the cat
    MAN = "Mannelijk"
    VROUW = "Vrouwelijk"
    ONBEKEND = "Onbekend"
    GESLACHT_CHOICES = [
        (MAN, "Mannelijk"),
        (VROUW, "Vrouwelijk"),
        (ONBEKEND, "Onbekend"),
    ]
    geslacht = models.CharField(max_length=200, 
                                choices=GESLACHT_CHOICES,
                                default=ONBEKEND)   
    
    # Age of the cat
    leeftijd = models.IntegerField(null=True)
    
    # Suitable for kids
    JA = "Ja"
    NEE = "Nee"
    ONBEKEND = "Onbekend"
    JA_NEE_CHOICES = [
        (JA, "Ja"),
        (NEE, "Nee"),
        (ONBEKEND, "Onbekend"),
    ]
    kanBijKinderen = models.CharField(max_length=200,
                                      choices=JA_NEE_CHOICES, 
                                      default=ONBEKEND)
    
    # Can live with dogs
    kanBijHonden = models.CharField(max_length=200,
                                      choices=JA_NEE_CHOICES,
                                      default=ONBEKEND)
    
    # Can live with cats
    kanBijKatten = models.CharField(max_length=200,
                                      choices=JA_NEE_CHOICES,
                                      default=ONBEKEND)
    
    # Has to go outside
    moetNaarBuiten = models.CharField(max_length=200,
                                      choices=JA_NEE_CHOICES,
                                      default=ONBEKEND)
    # Special needs
    BLIND = "Blind"
    DOOF = "Doof"
    MED = "Medicijnen"
    GEDR = "Behandeling gedragsproblemen"
    VOER = "Dieetvoer"
    ZORG_CHOICES = [
        (NEE, "Nee"),
        (ONBEKEND, "Onbekend"),
        (BLIND, "Blind"),
        (DOOF, "Doof"),
        (MED, "Medicijnen"),
        (GEDR, "Behandeling gedragsproblemen"),
        (VOER, "Dieetvoer"),
    ]
    
    specialeZorg = models.CharField(max_length=200,
                                    choices=ZORG_CHOICES,
                                    default=ONBEKEND)
     
    # Picture of the cat
    foto = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    
    # Available from
    beschikbaarVanaf = models.DateField(default=datetime.date.today)
    
    # Location
    locatie = models.CharField(max_length=40,
                               null=True)
    
    def __str__(self):
        return self.naam
    
    def save(self, *args, **kwargs):
        try:
            this = Kat.objects.get(id=self.id)
            if not(self.foto):
                self.foto = this.foto
        except: pass
        super(Kat, self).save(*args, **kwargs)