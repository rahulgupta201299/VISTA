#from django.contrib import admin
#from django.contrib import admin

# Register your models here.
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Waitlist


class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','created_at','updated_at')
    search_fields = ('first_name','last_name')
    #list_filter = ('is_student','is_admin','is_staff')
# Register your models here.
admin.site.register(Waitlist,WaitlistAdmin)