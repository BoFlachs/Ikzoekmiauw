from rest_framework import serializers
from . import models

class KatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kat
        fields = "__all__"

class KattenSoortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kattensoort
        fields = "__all__"