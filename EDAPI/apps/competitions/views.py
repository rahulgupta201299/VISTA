#from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
#from django.contrib.auth import get_user_model

#from .models import User
from .models import Competitions

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitions
        fields = ('name','year','created_at','updated_at')
        #extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    #def create(self, validated_data):
        #return get_user_model().objects.create_user(**validated_data)


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionSerializer