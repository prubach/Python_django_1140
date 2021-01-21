from django.urls import path, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path('', views.index, name='Index'),
    path('hello', views.hello, name='Hello'),
    path('<int:cust_id>/', views.show_customer, name='customer'),
    path('', include(router.urls))
]