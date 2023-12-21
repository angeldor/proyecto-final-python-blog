from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','subtitle', 'author','date', 'category', 'body','image')
        
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Aqui va el titulo de tu blog'}),
            'title_tag': forms.TextInput(attrs= {'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs= {'class': 'form-control','placeholder':'Aqui va el capitulo o el episodio'}),
            'author': forms.Select(attrs= {'class': 'form-control'}),
            'date': forms.DateInput(attrs= {'class': 'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control','placeholder':'Aqui va el contenido de tu posteo'}),
            # no logro hacer que se suban las imagenes
            # 'image': forms.ImageField(attrs={'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','subtitle', 'body','image')
        
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Aqui va el titulo de tu blog'}),
            'title_tag': forms.TextInput(attrs= {'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs= {'class': 'form-control','placeholder':'Aqui va el capitulo o el episodio'}),
            'date': forms.TextInput(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control','placeholder':'Aqui va el contenido de tu posteo'}),
            # 'image': forms.ImageField(attrs={'class':'form-control'})
        }