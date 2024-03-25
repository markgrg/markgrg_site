from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Это страница MAIN')

def categories(request):
    return HttpResponse('Это страница CATS')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')