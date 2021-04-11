from django.urls import path,include
from .views import *

urlpatterns = [
    path('pay/',PaymentView.as_view(),name="payment")
]
