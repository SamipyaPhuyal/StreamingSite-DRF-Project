from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class StreamingPlatform(models.Model):
    name=models.TextField(max_length=30)
    about=models.CharField(max_length=200)
    website=models.URLField(default="www.netflix.com")
    
    def __str__(self):
        return  self.name

class WatchList(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    platform=models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE,related_name="watchlist")
    avg_rating=models.FloatField(default=0)
    no_of_Ratings=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    description=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) +" "+ "stars"