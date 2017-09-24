from django.conf.urls import include, url
from django.contrib import admin
from .views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^index/', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    url(r'^room/', include('booking.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
