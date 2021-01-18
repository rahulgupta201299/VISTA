from rest_framework import serializers 
from . models import *

class ReactSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = React 
		fields = ('created_at','host','user','username', 'password') 

class CreateReactSerializer(serializers.ModelSerializer):
	class Meta:
		model=React
		fields=('user','username','password')
