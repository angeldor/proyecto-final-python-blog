from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','subtitle', 'author','date', 'body','image')
        
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Aqui va el titulo de tu blog'}),
            'title_tag': forms.TextInput(attrs= {'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs= {'class': 'form-control','placeholder':'Aqui va el capitulo o el episodio'}),
            'author': forms.Select(attrs= {'class': 'form-control'}),
            'date': forms.TextInput(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control','placeholder':'Aqui va el contenido de tu posteo'}),
        }