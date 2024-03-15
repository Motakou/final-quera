from django import forms
from .models import Critic, User

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['first_name', 'last_name', 'title', 'movie_title', 'text']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']