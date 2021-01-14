from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('hello', views.hello, name='Hello'),
]