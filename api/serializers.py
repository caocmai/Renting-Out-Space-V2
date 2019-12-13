from rest_framework.serializers import ModelSerializer

from listings.models import Listing

class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
