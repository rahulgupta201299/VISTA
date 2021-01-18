from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    #added1 start

    first_name = forms.CharField(max_length=255,required = True)
    last_name = forms.CharField(max_length = 255,required = True)

    #added1 end

    class Meta:
        model = User
        #fields = ['username','email','password1','password2'] #removed this is org
        #fields = ('username','first_name','last_name','email','password1','password2','phone_no','address','std','upload')
        fields = ['username','first_name','last_name','email','password1','password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email'] #removed this is org

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#added start
from .models import UserAdd
class UserAddForm(forms.ModelForm):
    class Meta:
        model = UserAdd
        fields = ['phone_no','address','std','upload']
        #fields = ['phone_no']
#added end
