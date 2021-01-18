from django.urls import path
from .views import StudentListView,StudentDetailView,StudentCreateView,StudentUpdateView,StudentDeleteView,UserStudentListView
from . import views
from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path('', StudentListView.as_view(), name = 'student-home'),
    path('credits/',views.credits, name = 'student-credits'),
    path('ann/<int:pk>/',StudentDetailView.as_view(),name = 'ann-detail'),
    path('ann/new/',StudentCreateView.as_view(),name = 'ann-create'),
    path('ann/<int:pk>/update/',StudentUpdateView.as_view(),name = 'ann-update'),
    path('ann/<int:pk>/delete/',StudentDeleteView.as_view(),name = 'ann-delete'),
    path('user/<str:username>', UserStudentListView.as_view(), name = 'user-posts'),
]
