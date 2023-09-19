from django.urls import path, include
from . import views   # Импортируем views.py из текущей директории приложения
from django.contrib.auth import views as auth_views

app_name = 'zoo'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('login_view', views.login_view, name='login_view'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('animals/<int:animal_id>', views.animal_details, name='animal_details'),
    path('animals', views.animals, name='animals'),
    path('about', views.about, name='about'),
    path('enclosures', views.enclosures, name='enclosures'),
    path('enclosures/<int:enclosure_id>', views.enclosure_details, name='enclosure_details'),
    path('profile', views.profile, name='profile'),
    path('staff_enclosures', views.staff_enclosures, name='staff_enclosures'),
    path('animals_food_consumption/<int:user_id>', views.animals_food_consumption, name='animals_food_consumption'),

    # Другие URL-маршруты для вашего приложения
]
