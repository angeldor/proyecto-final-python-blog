from typing import Any
from django.shortcuts import render
from django.http import request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class Home(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        
    
    
class ArtDetail(DetailView):
    model = Post
    template_name = 'artdetail.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArtDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields= '__all__'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
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
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(About, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
def pageNotFound(request, exception):
    return render(request,'404.html', status=404)