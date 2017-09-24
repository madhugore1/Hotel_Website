from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
import django_tables2 as tables
from .models import Reservation

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)


class ReviewBooking(tables.Table):
    class Meta:
        model = Reservation
        fields = ('user_id','room_id', 'check_in','check_out')
        attrs = {'class': 'table table-condensed'}

# table = ReviewBooking()

