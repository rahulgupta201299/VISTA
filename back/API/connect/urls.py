from django.urls import path
from .views import *

urlpatterns = [
    #path('room',RoomView.as_view()),
    path('create',ArticleAPIView.as_view())
]
