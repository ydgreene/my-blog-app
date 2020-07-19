from django.shortcuts import render
from django.utils import timezone 
from .models import Post 
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class HomeView(ListView):
	model = Post
	template_name = 'post_list.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'add_post.html'
	fields = '__all__'

	