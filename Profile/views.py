from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,viewsets,mixins
from rest_framework.views import APIView
from .serializer import *
from django.http import JsonResponse,HttpResponse
# Create your views here.
class ProfileView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Profile.objects.all().order_by("-id")
    serializer_class=ProfileSerializer
    lookup_field="id"
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
    def post(self,request,*args,**kwargs):
        email=request.data['email']
        firstname=request.data['firstname']
        lastname=request.data['lastname']
        Address1=request.data['Address1']
        Address2=request.data['Address2']
        Zip=request.data['Zip']
        state=request.data['state']
        city=request.data['city']
        DOB=request.data['DOB']
        gender=request.data['gender']
        school=request.data['school']
        grade=request.data['grade']
        query=Profile.objects.filter(email=email)
        if query.exists():
            x=Profile.objects.get(email=email)
            if len(firstname):
                x.firstname=firstname.upper()
            if len(lastname):
                x.lastname=lastname.upper()
            if len(Address1):
                x.Address1=Address1.upper()
            if len(Address2):
                x.Address2=Address2.upper()
            if len(Zip):
                x.Zip=Zip
            if len(state):
                x.state=state.upper()
            if len(city):
                x.city=city.upper()
            if len(DOB):
                L=[]
                L=DOB.split('-')
                x.DOB=L[2]+"-"+L[1]+"-"+L[0]
            if len(gender):
                x.gender=gender.upper()
            if len(school):
                x.school=school.upper()
            if len(grade):
                x.grade=grade.upper()
            x.save()
            return JsonResponse({'message':'user is updated','Error':''},status=200)
        else:
            Profile.objects.create(email=email,firstname=firstname,lastname=lastname,Address1=Address1,Address2=Address2,Zip=Zip,state=state,city=city,DOB=DOB,gender=gender,school=school,grade=grade)
            return JsonResponse({'message':'Profile is created','Error':''},status=200)
        return JsonResponse({'Error': 'Not updated some Error occured. Try Again!','message':''},status=200)