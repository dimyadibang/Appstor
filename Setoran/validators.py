from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *

def validate_kitab(value):
    if Setoran.objects.filter(kitab__exact=value).exists:
        raise serializers.ValidationError("Data telah ada")
    return value


def validate_mahasantri(value):
    if Setoran.objects.filter(mahasantri__exact=value).exists:
        raise serializers.ValidationError("Data telah ada")
    return value


        

uniqueSetoran=UniqueValidator(queryset=Setoran.objects.all())