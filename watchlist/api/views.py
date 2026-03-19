from django.shortcuts import render
from watchlist.models import WatchList,StreamingPlatform,Review,User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from watchlist.api.serializers import WatchListSerializer,StreamingPlatformSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from watchlist.api.permissions import UserReReview

class ReviewList(generics.ListCreateAPIView):
    serializer_class=ReviewSerializer
    def  get_queryset(self,**kwargs):
        pk=self.kwargs.get('pk')
        watch=WatchList.objects.get(pk=pk)
        serializer=watch.reviews
        return serializer
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        watch=WatchList.objects.get(pk=pk)
        author=self.request.user
        review_set=Review.objects.filter(watchlist=watch,author=author)
        if review_set.exists():
            raise ValidationError(
                {"detail": "You have already done a review for this!"}
            )
        if watch.no_of_Ratings==0:
            watch.avg_rating=serializer.validated_data['rating']
        else:
            watch.avg_rating=(watch.avg_rating+serializer.validated_data['rating'])/2
        watch.no_of_Ratings=watch.no_of_Ratings+1
        watch.save()
        serializer.save(watchlist=watch,author=author)        
        
        
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated,UserReReview]
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()
          
          
class WatchListAV(APIView):
    def get(self,request):
        movie=WatchList.objects.all()
        serializer =WatchListSerializer(movie,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
    def delete(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except:
            return Response(status=404)
        movie.delete()
        return Response(status=204)

