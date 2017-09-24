from .models import RoomType
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CheckForm(forms.Form):
    check_in = forms.DateField()
    check_out = forms.DateField()

