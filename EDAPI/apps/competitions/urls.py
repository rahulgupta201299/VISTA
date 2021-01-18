from django.urls import path, include
from rest_framework import routers
from .views import CompetitionViewSet

router = routers.DefaultRouter()
router.register(r'', CompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]