from rest_framework import serializers
from .models import City, RealEstateOffer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RealEstateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateOffer
        fields = '__all__'
