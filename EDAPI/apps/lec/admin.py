from django.contrib import admin

# Register your models here.
#from django.contrib import admin
#from django.contrib import admin

# Register your models here.
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Lec


class LecAdmin(admin.ModelAdmin):
    list_display = ('title','lec_name','created_at','updated_at','date')
    search_fields = ('title','lec_name')
    #list_filter = ('is_student','is_admin','is_staff')
# Register your models here.
admin.site.register(Lec,LecAdmin)