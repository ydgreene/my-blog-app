from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterview(generic.CreateView):
	form_class = UserCreationForm
	template = 'registration/register.html'
	success_url = reverse_lazy('login')