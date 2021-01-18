from django.urls import path, include
from rest_framework import routers
from .views import LecViewSet

router = routers.DefaultRouter()
router.register(r'', LecViewSet)

urlpatterns = [
    path('', include(router.urls)),
]