from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer

# Create your views here.


def index(request):
    return HttpResponse('Welcome to My Bank!!!')


def hello(request):
    msg = 'Hello Text inside a template'
    return render(request, 'test.html', {'hello_text': msg})


def show_customer(request, cust_id):
    customer = get_object_or_404(Customer, pk=cust_id)
    return render(request, 'cust.html', {'customer': customer})