from django.shortcuts import render
from django.http import request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
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
    
def CategoryView(request, cats):
    return render(request, 'categories.html', {'cats':cats})
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields= '__all__'
    
class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editpost.html'
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')
    
class About(TemplateView):
    template_name= 'about.html'
    
def pageNotFound(request, exception):
    return render(request,'404.html', status=404)