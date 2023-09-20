from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Animal, Enclosure, Employee, CustomUser, FoodConsumption, News
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import requests
from django.contrib.auth import logout


def index(request):
    # Представление для отображения информации о зоопарке
    news = News.objects.latest('publication_date')
    animals = Animal.objects.all()
    enclosures = Enclosure.objects.all()
    joke = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    cat = requests.get('https://catfact.ninja/fact').json()
    context = {
        'news': news,
        'animals': animals,
        'enclosures': enclosures,
        'joke': joke,
        'cat': cat
    }
    return render(request, 'index.html', context)

def animals(request):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }
    return render(request, 'animals.html', context)

def enclosures(request):
    enclosures = Enclosure.objects.all()
    context = {
        'enclosures': enclosures
    }
    return render(request, 'enclosures.html', context)

def about(request):
    return render(request, 'about.html')

def animal_details(request, animal_id):
    # Представление для отображения детальной информации о животном
    animal = Animal.objects.get(pk=animal_id)
    context = {
        'animal': animal,
    }
    return render(request, 'animal_details.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birth_date = request.POST['birth_date']

        if datetime.now().date().year - datetime.strptime(birth_date, "%Y-%m-%d").year < 18:
            error_message = "Пользователю должно быть больше 18 лет"
            return render(request, 'register.html', {'error_message': error_message})


        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует. Вам необходимо войти.')
            return redirect('/login')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            birth_date=birth_date
        )

        login(request, user)
        return redirect('/profile')  # Перенаправление на страницу профиля или другую страницу по вашему выбору

    return render(request, 'register.html')

def logout_view(request):
    # Выход пользователя из системы
    logout(request)
    return redirect('/index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            error_message = "Неправильное имя пользователя или пароль."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def enclosure_details(request, enclosure_id):
    # Представление для отображения детальной информации о животном
    enclosure = Enclosure.objects.get(pk=enclosure_id)
    context = {
        'enclosure': enclosure,
    }
    return render(request, 'enclosure_details.html', context)

@login_required
def profile(request):
    # Представление для отображения профиля пользователя
    user = request.user

    if user.is_staff and Employee.objects.filter(user=user).exists():
        employee = Employee.objects.get(user=user)
        assigned_enclosure = Enclosure.objects.filter(employee__user=user)
        context = {
            'user': user,
            'employee': employee,
            'assigned_enclosure': assigned_enclosure,
        }
        return render(request, 'employee_profile.html', context)
    else:
        context = {
            'user': user,
        }
        return render(request, 'user_profile.html', context)

def staff_enclosures(request):
    if request.user.is_staff:
        user = request.user
        assigned_enclosure = Enclosure.objects.filter(employee__user=user)
        context = {
            'user': user,
            'assigned_enclosure': assigned_enclosure,
        }
        return render(request, 'staff_enclosures.html', context)
    else:
        error_message = "Пользователь не является сотрудником."
        return render(request, 'staff_enclosures.html', {'error_message': error_message})

def animals_food_consumption(request):
    if request.user.is_staff:
        selected_animal_id = request.GET.get('selected_animal_id', None)
        selected_date = request.GET.get('selected_date', None)
        print(selected_date)

        if selected_animal_id != "" and selected_date != "":
            animal = Animal.objects.get(pk=selected_animal_id)
            food_consumptions = FoodConsumption.objects.filter(animal=animal).filter(date=selected_date)
        else:
            animal = None
            food_consumptions = []

        user = request.user
        animals = Animal.objects.filter(user=user)
        context = {
            'animals': animals,
            'selected_animal': animal,
            'food_consumptions': food_consumptions,
        }

        return render(request, 'animals_food_consumption.html', context)

    else:
        error_message = "Пользователь не является сотрудником."
        return render(request, 'animals_food_consumption.html', {'error_message': error_message})

def news(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)
    context = {
        'news': news,
    }
    return render(request, 'news_detail.html', context)

@staff_member_required
def superuser_view(request):
    # Представление, доступное только суперпользователю
    return render(request, 'superuser_view.html')

