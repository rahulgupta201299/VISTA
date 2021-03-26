from django.shortcuts import render
from .serializers import *
from rest_framework import generics,mixins,viewsets
from . models import *
from rest_framework.response import Response
# Create your views here.
class BlogView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=BlogDetail.objects.all().order_by("-id")
    serializer_class=BlogSerializer
    lookup_field="id"
    
    def get(self,request,id=None):
        return self.list(request)