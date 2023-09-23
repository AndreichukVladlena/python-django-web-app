from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Animal, Enclosure, Employee, CustomUser, FoodConsumption, News, AnimalSpecies, AnimalClass, \
    HabitatCountry, EmployeePosition, Food, JobVacancy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import requests
from django.contrib.auth import logout
from django.utils import timezone 


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
    query = request.GET.get('q')
    animals = Animal.objects.all().order_by('name')
    enclosures = Enclosure.objects.all()

    if request.method == "POST":
        if request.POST.get("selected_enclosure_id")!="all":
            enclosure = Enclosure.objects.get(id=request.POST.get("selected_enclosure_id"))
            animals = enclosure.animals.all()

    if query:
        animals = animals.filter(Q(name__icontains=query) |
            Q(facts__icontains=query))

    context = {
        'animals': animals,
        'enclosures': enclosures,
    }
    return render(request, 'animals.html', context)

def enclosures(request):
    query = request.GET.get('q')
    enclosures = Enclosure.objects.all().order_by('name')

    if query:
        enclosures = enclosures.filter(name__icontains=query)

    context = {
        'enclosures': enclosures
    }
    return render(request, 'enclosures.html', context)

def employees(request):
    employees = Employee.objects.all().order_by('user')

    context = {
        'employees': employees
    }
    return render(request, 'employees.html', context)

def about(request):
    return render(request, 'about.html')

def politics(request):
    return render(request, 'politics.html')

def certificate(request):
    return render(request, 'certificate.html')



def animal_details(request, animal_id):
    # Представление для отображения детальной информации о животном
    animal = Animal.objects.get(pk=animal_id)
    unique_foods = Food.objects.filter(animal=animal).values('name', 'composition').distinct()

    context = {
        'animal': animal,
        'unique_foods': unique_foods,
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

        if selected_animal_id is not None and selected_animal_id != "" and selected_date != "":
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
    query = request.GET.get('q')

    news_list = News.objects.all()

    if query:
        news_list = news_list.filter(title__icontains=query)

    context = {
       'news_list': news_list,
    }
    return render(request, 'news_list.html', context)

def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)
    context = {
        'news': news,
    }
    return render(request, 'news_detail.html', context)

@staff_member_required
def edit_animal(request, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
        animal_countries = animal.habitat_countries
        species = AnimalSpecies.objects.all()
        classes = AnimalClass.objects.all()
        countries = HabitatCountry.objects.all()
        context = {
            'animal': animal,
            'animal_countries': animal_countries,
            'species': species,
            'classes': classes,
            'countries': countries,
        }
        if request.method == "POST":
            animal.species = AnimalSpecies.objects.get(id=request.POST.get("selected_specie_id"))
            animal.classes = AnimalClass.objects.get(id=request.POST.get("selected_class_id"))
            animal.habitat_countries.clear()
            animal.habitat_countries.set(request.POST.getlist("country"))
            animal.save()
            return redirect('/animals')
        else:
            return render(request, "edit_animal.html", context)
    except Animal.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

    return render(request, 'edit_animal.html')

@staff_member_required
def edit_profile(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        employee_enclosures = employee.assigned_enclosure
        enclosures = Enclosure.objects.all()
        positions = EmployeePosition.objects.all()

        context = {
            'employee': employee,
            'employee_enclosures': employee_enclosures,
            'enclosures': enclosures,
            'positions': positions,
        }

        if request.method == "POST":
            employee.phone_number = request.POST.get("phone_number")
            employee.assigned_enclosure.clear()
            employee.assigned_enclosure.set(request.POST.getlist("enclosures"))
            employee.position = EmployeePosition.objects.get(id=request.POST.get("selected_position_id"))
            employee.save()
            return redirect('/profile')
        else:
            return render(request, "edit_profile.html", context)
    except Animal.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

    return render(request, 'edit_profile.html')

def job_vacancies(request):
    vacancies = JobVacancy.objects.all()
    return render(request, 'job_vacancies.html', {'vacancies': vacancies})