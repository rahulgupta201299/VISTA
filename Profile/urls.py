from django.urls import path,include
from .views import *
urlpatterns = [
    path('detail/',ProfileView.as_view(),name="profile"),
    path('detail/<int:id>/',ProfileView.as_view(),name="profile"),
]
