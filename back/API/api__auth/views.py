from django.shortcuts import render

# Create your views here.
from .models import Database
from .serializer import Registration
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from rest_framework import status
import json
from django.conf import settings
import random,string
from django.views.decorators.csrf import ensure_csrf_cookie


#from django.template.loader import render_to_string
#from verify_email.email_handler import send_verification_email
#from django.core.mail import send_mail
import smtplib

 
class DataAPIView(APIView):
    serializer_class=Registration
    def get(self, request):
        detail = [ {"date":detail.date,"firstName": detail.firstName,"lastName": detail.lastName,"email":detail.email,"phone":detail.phone,"state":detail.state,"pin":detail.pin}  
        for detail in Database.objects.all()] 
        return Response(detail) 
        """
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
        """
        
    #@ensure_csrf_cookie
    def post(self, request):
        serializer = Registration(data=request.data) 
        
        if serializer.is_valid(raise_exception=True): 
            print(request.data)
            email=serializer.validated_data.get('email')
            queryset=Database.objects.filter(email=email)
            if queryset.exists():
                #inactive_user = send_verification_email(request, form)
                return JsonResponse({"Error":"User Already Exists. Please Login!"},status=status.HTTP_302_FOUND)
            else:
                """
                email_subject='Activate your account'
                serializer.is_active=False
                letters = string.digits
                otp= ( ''.join(random.choice(letters) for i in range(10)) )
                server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                server.login("rg810943@gmail.com",'Rahul@1234')
                server.sendmail("rg810943@gmail.com",email,f"Activate your account{otp}")
                server.quit()
                """
                serializer.save() 
                return JsonResponse(serializer.data,status=status.HTTP_200_OK)

        return JsonResponse({"Error":"user already exist"},status=status.HTTP_400_BAD_REQUEST)

"""
serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

"""