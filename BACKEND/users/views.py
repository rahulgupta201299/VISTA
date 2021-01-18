from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
import os
from django.core.mail import send_mail
from .forms import UserAddForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import UsersSerializer      # add this
from django.contrib.auth.models import User               # add this
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    print(request.POST)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #added start
        add_form = UserAddForm(request.POST)
        #added end
        if form.is_valid() and add_form.is_valid():
        #if form.is_valid(): #origi
            #form.save()#origi
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account for {username} has been created. You can now login with the registered credentials. Mail will be recieved on the registered email. A reciept in pdf form is also given.')
            #added start
            data = request.POST.copy()
            emails = data.getlist('email')
            subject = 'Thank you for signing up.'
            from_email = 'emailtestingfordjango@gmail.com'
            message = 'Welcome to edtech. Your username is '+data.getlist('username')[0]+'.'
            send_mail(subject,message,from_email,emails,False)
            #added end
            #added2 start
            user = form.save()
            add = add_form.save(commit=False)
            add.user = user
            add.save()
            #added2 end
            return redirect('login')
    else:
        #print(request.POST.get(data))
        form = UserRegisterForm()
        #added start
        add_form = UserAddForm()
        #added end
    #return render(request,'users/register.html',{'form':form}) #origi
    return render(request,'users/register.html',{'form':form,'add_form':add_form})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request,'users/profile.html',context)

    """
class UserViewSet(viewsets.ModelViewSet):

    API endpoint that allows users to be viewed or edited.

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

"""

"""
class U_view(viewsets.ModelViewSet):       # add this
  serializer_class = UsersSerializer          # add this
  queryset = User.objects.all()              # add this
"""