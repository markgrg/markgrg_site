from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse


menu = [{'title': 'Добавить статью', 'url_name': 'addpost'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

data_db = [
    {'post_name_id': 'python_post', 'title': 'Python', 'content': 'Где применаяется язык Python', 'is_published': True},
    {'post_name_id': 'JavaScript_post', 'title': 'Java Script', 'content': 'Где применаяется язык Java Script', 'is_published': False},
    {'post_name_id': 'C++_post', 'title': 'C++', 'content': 'Где применаяется язык C++', 'is_published': True},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'index_main.html', context=data) 

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    return render(request, 'about.html', {"title": 'О нас'})

def show_post(request, post_name_id):
    return HttpResponse(f'Отображение статьи {post_name_id}')

def addpost(request):
    return HttpResponse(f'Добавление поста')

def show_post(request, post_name_id):
    return HttpResponse(f'Отображение статьи {post_name_id}')

def contact(request):
    return HttpResponse(f'Обратная связь')

def login(request):
    return HttpResponse(f'Авторизация')