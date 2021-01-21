from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Account
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions

from .serializers import UserSerializer, GroupSerializer, CustomerSerializer, AccountSerializer

# Create your views here.


def index(request):
    return HttpResponse('Welcome to My Bank!!!')


def hello(request):
    msg = 'Hello Text inside a template'
    return render(request, 'test.html', {'hello_text': msg})


def show_customer(request, cust_id):
    customer = get_object_or_404(Customer, pk=cust_id)
    return render(request, 'cust.html', {'customer': customer})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
