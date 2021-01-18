#from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

#from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email', 'password','is_student')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        #return get_user_model().objects.create_user(**validated_data)
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

#added for email

from django.shortcuts import render
from django.core.mail import send_mail

def sendmail(request):
    message_name = request.POST['message_name']
    message_email = request.POST['message_email']
    

    if request.method == "POST":
        send_mail("Welcome to Vista","You are successfully registered.",['djangoapivista@gmail.com'],message_email)


#added end for email

