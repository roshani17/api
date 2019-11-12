from rest_framework import serializers
from .models import destination

class destinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = destination
        fields = '__all__'