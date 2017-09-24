# bookings/urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^check_availability', views.CheckFormView.as_view(), name='check_availability '),
]
