
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from watchlist.api.views import (ReviewDetail,WatchListAV,WatchDetailAV,
ReviewList)
# router=DefaultRouter()
# router.register("stream",StreamPlatformVS,basename="stream")
urlpatterns = [
    path("list/",WatchListAV.as_view(),name="movie-list"),
    path("<int:pk>",WatchDetailAV.as_view(),name="movie-detail"),
    # path("",include(router.urls)),
    # path("stream/",StreamingPlatformAV.as_view(),name="stream"),
    # path("stream/detail/<int:pk>",StreamDetailAV.as_view(),name="stream-detail"),
    path("<int:pk>/reviews/",ReviewList.as_view(),name="review-list"),
    path("review/<int:pk>/",ReviewDetail.as_view(),name="review-detail"),
]