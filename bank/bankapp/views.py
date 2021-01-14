from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Welcome to My Bank!!!')


def hello(request):
    msg = 'Hello Text inside a template'
    return render(request, 'test.html', {'hello_text': msg})