from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea


class UserAdminConfig(admin.ModelAdmin):
    
    search_fields = ('email', 'user_name', 'department', 'rank')
    list_filter = ('department', 'rank')
    list_display = ('email', 'user_name','department', 'rank')
    


admin.site.register(NewUser, UserAdminConfig)
