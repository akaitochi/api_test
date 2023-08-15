from django.urls import path
from .views import someitems, ping

urlpatterns = [
    path('api/v1/someitems/', someitems, name='someitems'),
    path('api/v1/ping/', ping, name='ping'),
               ]
