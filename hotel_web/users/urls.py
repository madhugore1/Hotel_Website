# users/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login', views.LoginFormView.as_view(), name='login'),
    url(r'^register', views.UserFormView.as_view(), name='register'),
    url(r'^logout', views.logout_view, name='logout'),
]
