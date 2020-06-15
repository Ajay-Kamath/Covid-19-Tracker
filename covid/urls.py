from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts', views.index, name='index')
]