from django.contrib import admin
from django.urls import path,include,re_path
from .views import *
from rest_framework import routers

route=routers.DefaultRouter()
#route.register("blogpost",BlogView,basename="BlogView")
urlpatterns = [
    #path("",include(route.urls)),
    path('new/',BlogView.as_view(),name="blogging"),
]
