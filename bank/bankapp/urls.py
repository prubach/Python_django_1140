from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('hello', views.hello, name='Hello'),
    path('<int:cust_id>/', views.show_customer, name='customer')
]