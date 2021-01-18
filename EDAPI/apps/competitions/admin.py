#from django.contrib import admin
#from django.contrib import admin

# Register your models here.
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Competitions


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
    search_fields = ('name',)
    #list_filter = ('is_student','is_admin','is_staff')
# Register your models here.
admin.site.register(Competitions,CompetitionAdmin)