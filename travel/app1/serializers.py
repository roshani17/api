from rest_framework import serializers
from .models import destination, destinationName
from django.contrib.auth.models import User

class destinationSerializer(serializers.ModelSerializer):
    disc = serializers.CharField(required=False)
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = destination
        fields = ('name','disc', 'price','owner','owner_id')

class destinationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = destinationName
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    destination = serializers.PrimaryKeyRelatedField(many=True, queryset=destination.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'destination']