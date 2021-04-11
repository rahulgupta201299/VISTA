from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,viewsets,mixins
from rest_framework.views import APIView
from .serializer import *
from django.http import JsonResponse,HttpResponse
import razorpay
# Create your views here.
class PaymentView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=PaymentSerializer
    queryset=Payment.objects.all().order_by("-id")
    lookup_field="id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request,*args,**kwargs):
        name=request.data['name']
        email=request.data['email']
        amount=int(request.data['Amount'])*100
        courseName=request.data['courseName']
        courseID=request.data['courseID']

        client=razorpay.Client(auth=("rzp_test_a3n3ow4GPvzy2m","xZ20n3FUYfcPJWkKpRhCMs3w"))
        payment=client.order.create({'amount':amount,'currency':'INR' ,'payment_capture':'1'})
        print(payment)
        pay=Payment(name=name,email=email,courseName=courseName,courseID=courseID,amount=amount,payment_id=payment['id'])
        return JsonResponse({'message':'paid'},status=200)