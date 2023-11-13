from django import forms
from .models import BlogPost

# Create a form to add a new blog post
class BlogPostForm(forms.ModelForm): # ModelForm is a form that is tied to a model
    class Meta: 
        model = BlogPost
        fields = ['title', 'content']
        labels = {'title': 'Title of your post', 'content': 'Content'}