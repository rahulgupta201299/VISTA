from django.contrib import admin
#added1 start
from .models import UserAdd
admin.site.register(UserAdd)
#added1 end
# Register your models here.
from .models import Profile
admin.site.register(Profile)
