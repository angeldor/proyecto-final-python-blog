from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import SingUpForm


class SingUp(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registro/singup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'registro/login.html'