from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Animal, Enclosure, Employee, CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import requests
from django.contrib.auth import logout


def index(request):
    # Представление для отображения информации о зоопарке
    animals = Animal.objects.all()
    enclosures = Enclosure.objects.all()
    joke = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    cat = requests.get('https://catfact.ninja/fact').json()
    context = {
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

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует. Вам необходимо войти.')
            return redirect('/login')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
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
        # assigned_enclosure = employee.assigned_enclosure.all()
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

@staff_member_required
def superuser_view(request):
    # Представление, доступное только суперпользователю
    return render(request, 'superuser_view.html')

