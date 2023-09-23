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
    path('animals_food_consumption', views.animals_food_consumption, name='animals_food_consumption'),
    path('edit_animal/<int:animal_id>', views.edit_animal, name='edit_animal'),
    path('employees', views.employees, name='employees'),
    path('edit_profile/<int:employee_id>', views.edit_profile, name='edit_profile'),

    path('news_list', views.news, name='news'),
    path('news_detail/<int:news_id>', views.news_detail, name='news_detail'),
    path('politics', views.politics, name='politics'),
    path('certificate', views.certificate, name='certificate'),
    path('job_vacancies', views.job_vacancies, name='job_vacancies'),
    path('faq', views.faq, name='faq'),
    path('add_question', views.add_question, name='add_question'),
    path('reviews', views.reviews, name='reviews'),
    path('add_review', views.add_review, name='add_review'),
    path('coupons', views.coupons, name='coupons'),




    # Другие URL-маршруты для вашего приложения
]
