# blog/forms.py
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'text',)
    category = forms.ChoiceField(choices=Post.CATEGORY_LIST, required=True,
                                     widget=forms.Select(attrs={'class': 'form-control'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
