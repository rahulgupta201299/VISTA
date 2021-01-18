from django.urls import path, include 
from .views import *
urlpatterns = [
    path('register/',DataAPIView.as_view(),name="react")
]
