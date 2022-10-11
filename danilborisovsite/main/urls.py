from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('contactme', views.contactme, name='contactme'),
    path('expireance', views.expireance, name='expireance'),
]
