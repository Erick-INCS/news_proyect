from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationform(UserCreationForm):
    """
    docstring
    """
    class Meta(UserCreationForm):
        """
        docstring
        """
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', 'nice_name',)
        fields = ('username', 'email', 'age',)
        

class CustomUserChangeForm(UserChangeForm):
    """
    docstring
    """
    class Meta(UserChangeForm):
        """ docstring """
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',)