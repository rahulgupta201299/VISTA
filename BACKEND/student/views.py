from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models  import Student
from django.contrib.auth.models import User


#add this to the present student/views.py

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from login_registeration_edit_prof.serializers import UserSerializer, GroupSerializer      
#please check the app name in ur folder structure to check the first name


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



def home(request):
    context = {
    'anns':Student.objects.all()
    }
    return render(request,'student/home.html',context)



class StudentListView(ListView):
    model = Student
    template_name = 'student/home.html'
    context_object_name = 'anns'
    paginate_by = 2


class UserStudentListView(ListView):
    model = Student
    template_name = 'student/user_posts.html'
    context_object_name = 'anns'
    ordering = ['-date_posted']
    paginate_by = 2
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Student.objects.filter(author = user).order_by('-date_posted')






class StudentDetailView(DetailView):
    model = Student



class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Student
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class StudentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Student
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def credits(request):
    return render(request,'student/credits.html',{'title':'Credits'})
# Create your views here.
