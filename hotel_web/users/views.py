from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import *


def register(request):
    template = loader.get_template("users/register.html")
    return HttpResponse(template.render({}, request))


def log_in(request):
    template = loader.get_template("users/login.html")
    return HttpResponse(template.render({}, request))


def logout_view(request):
    logout(request)
    return redirect('/index')
    #return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = AuthenticationForm(data=request.POST)
        print form.errors
        if form.is_valid():
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/index/')

        return render(request, self.template_name, {'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = 'users/register.html'


    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/index/')

        return render(request, self.template_name, {'form': form})

