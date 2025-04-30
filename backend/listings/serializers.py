from rest_framework import serializers
from .models import Listing, Host

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    host = HostSerializer()

    class Meta:
        model = Listing
        fields = '__all__'
