from rest_framework import serializers
from watchlist.models import WatchList,StreamingPlatform,Review
from django.core.exceptions import ValidationError

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
        read_only_fields=["watchlist","author"]
        
class WatchListSerializer(serializers.ModelSerializer):
    reviews=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields="__all__"
        

class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=StreamingPlatform
        fields="__all__"

