from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationform

# Create your views here.
class SignUpView(CreateView):
    form_class= CustomUserCreationform
    success_url = reverse_lazy('login')
    template_name='registration/signup.html'