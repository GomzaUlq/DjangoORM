from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game


def home(request):
    title = 'Главная страница'
    home_page = 'Главная'
    magazine_tea = 'Магазин'
    product_cart = 'Корзина'
    context = {
        'title': title,
        'home_page': home_page,
        'magazine_tea': magazine_tea,
        'product_cart': product_cart,

    }
    return render(request, 'four_task/home.html', context)


def magazine(request):
    game = 'Игры'
    buy = 'Купить'
    games = Game.objects.all()
    context = {
        'game': game,
        'games': games,
        'buy': buy,
    }
    return render(request, 'four_task/tea.html', context)


def cart(request):
    title = 'Вы еще не добавили товар'
    context = {
        'title': title,
    }
    return render(request, 'four_task/cart.html', context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(username)

            if password == repeat_password:
                existing_users = Buyer.objects.all()
                user_exists = False
                for user in existing_users:
                    if user.name == username:
                        user_exists = True
                        break
                if not user_exists:
                    Buyer.objects.create(name=username, age=age, balance=5000)
                    return HttpResponse(f'Приветствуем, {username}!')
                else:
                    info['error'] = 'Пользователь с таким именем уже существует'
            else:
                info['error'] = 'Пароли не совпадают'
    else:
        form = UserRegister()
    return render(request, 'four_task/registrarion_page.html', {'form': form, 'info': info})
