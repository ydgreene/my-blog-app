from django.shortcuts import render
from django.utils import timezone 
from .models import Post 
from django.views.generic import ListView, DetailView
# Create your views here.

class HomeView(ListView):
	model = Post
	template_name = 'post_list.html'


	