from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Это страница MAIN')

def categories(request):
    return HttpResponse('Это страница CATS')

