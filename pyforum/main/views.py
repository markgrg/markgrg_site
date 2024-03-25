from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'index_main.html', context=data) 

def categories(request):
    return HttpResponse('Это страница CATS')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    return render(request, 'about.html', {"title": 'О нас'})