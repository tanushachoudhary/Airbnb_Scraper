from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing, Host
from .serializers import ListingSerializer

@api_view(['GET'])
def get_listings(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_listing(request):
    host_data = request.data.pop('host')
    host, _ = Host.objects.get_or_create(**host_data)
    listing = Listing.objects.create(host=host, **request.data)
    return Response({"message": "Listing added successfully", "id": listing.id})
