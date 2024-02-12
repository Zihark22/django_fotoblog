from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True) # pour envoie formulaire séparé sur la même page
    title = forms.CharField(label='Titre', min_length=5, max_length=150, error_messages={'required': 'Entrez le titre'})  
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 15, 'cols': 100}),label='Description', min_length=5, max_length=5000, error_messages={'required': 'Entrez la descritpion'})  

    class Meta:
        model = models.Blog
        fields = ['title', 'content']
        
        
class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)