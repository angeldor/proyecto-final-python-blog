from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']
    
class ArtDetail(DetailView):
    model = Post
    template_name = 'artdetail.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    
class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editpost.html'
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')