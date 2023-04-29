from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Homework


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget = forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label='Password2',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )


class loginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
                'class': 'form-control'
        }) 
    )
    password = forms.CharField(
        label ='Password',
        widget= forms.PasswordInput(attrs={
                'class': 'form-control'
        })
    )


class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'content', 'deadline', 'image', 'lesson')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content":forms.Textarea(attrs={"class": "form-control"}),
            "deadline":forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            "image": forms.ClearableFileInput(),
            "lesson": forms.Select(attrs={"class": "form-control"})
        }
        
        
