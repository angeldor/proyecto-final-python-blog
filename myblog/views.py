from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'
    
class ArtDetail(DetailView):
    model = Post
    template_name = 'artdetail.html'
    
class AddPost(CreateView):
    model = Post
    template_name = 'addpost.html'
    fields = '__all__'