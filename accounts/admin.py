from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationform, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    docstring
    """
    add_form = CustomUserCreationform
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'nice_name',]
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'nice_name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'nice_name',)}),
    )
    
    
    
admin.site.register(CustomUser, CustomUserAdmin)