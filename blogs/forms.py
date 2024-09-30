from django import forms
from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        labels = {'title': 'blog title'}
       
        widgets = {'description': forms.Textarea(attrs={'cols': 50})}

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {'content': forms.Textarea(attrs={'cols': 50})}