from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)
