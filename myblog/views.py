from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm


class Home(ListView):
    model = Post
    template_name = 'home.html'
    
class ArtDetail(DetailView):
    model = Post
    template_name = 'artdetail.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    
class EditPost(UpdateView):
    model = Post
    template_name = 'editpost.html'
    fields = ['title', 'title_tag', 'body']