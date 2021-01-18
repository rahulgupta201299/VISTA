# users/serializers.py
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('user','phone_no','address','std','upload')