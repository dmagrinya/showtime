from rest_framework import serializers
from app.models import Venue, Artist
from django.contrib.auth.models import User



class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ['name']



class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Artist
        fields = ['name', 'owner']



class UserSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'artists']
