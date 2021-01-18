from rest_framework import serializers
from .models import Database
 
 
 
class Registration(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = ['date','firstName', 'lastName','email','phone','state','pin','password']
