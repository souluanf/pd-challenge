from rest_framework import serializers
from place.models import Place


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ('id', 'name', 'slug', 'city', 'state',)

    def create(self, validated_data):
        place = Place.objects.create(**validated_data)
        return place

