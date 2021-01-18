from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics,status
from rest_framework.response import Response 
from . serializer import *
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here. 

class ArticleAPIView(APIView):
	def get(self,request):
		articles=React.objects.all()
		serializer=CreateReactSerializer(articles,many=True)
		return JsonResponse(serializer.data,safe=False)
	def post(self,request):
		data=JSONParser().parse(request)
		serializer=CreateReactSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors,status=400)



"""
@csrf_exempt
def article_list(request):
	if request.method=='GET':
		articles=React.objects.all()
		serializer=ReactSerializer(articles,many=True)
		return JsonResponse(serializer.data,safe=False)
		
	elif request.method=='POST':
		data=JSONParser().parse(request)
		serializer=ReactSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors,status=400)








class RoomView(generics.ListAPIView):
	queryset=React.objects.all()
	serializer_class=ReactSerializer

class CreateRoomView(APIView): 
	serializer_class = CreateReactSerializer
	x='code'

	def get(self,request):
		code=request.GET.get(self.x)
		print(code)

	def post(self,request):
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)


	def post(self,request,format=None):
		if not self.request.session.exists(self.request.session.session_key):
			self.request.session.create()
		
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid():
			user=serializer.data.get('user')
			username=serializer.data.get('username')
			password=serializer.data.get('password')
			host=self.request.session.session_key
			queryset=React.objects.filter(host=host)
			if queryset.exists():
				room=queryset[0]
				room.user=user
				room.username=username
				room.password=password
				room.save(ReactSerializer(room).data,status=status.HTTP_200_OK)
			else:
				room=React(host=host,user=user,username=username,password=password)
				room.save()
				return Response(ReactSerializer(room).data,status=status.HTTP_201_CREATED)
		return Response({'Bad Request':'Invalid data...'},status=status.HTTP_400_BAD_REQUEST)
"""