from django import forms
from .models import Critic, User

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['creator_first_name', 'creator_last_name','title', 'movie_title', 'text']

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
