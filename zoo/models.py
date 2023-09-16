from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

class Food(models.Model):
    name = models.CharField(max_length=100)
    specie = models.CharField(max_length=100, default="Приматы")

    def __str__(self) :
        return f'{self.name}'

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    entry_date = models.DateField()
    birth_year = models.IntegerField()
    photo = models.ImageField(upload_to='animal_photos/', default='animal_photos/defPic.jpeg')
    facts = models.TextField()
    food = models.ManyToManyField(Food, through='FoodConsumption')

    def __str__(self) :
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('zoo:animal_details', args=[str(self.id)])

class FoodConsumption(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField()
    daily_amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) :
        return f'{self.animal.name}, {self.food.name}, {self.date}'

class Enclosure(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    has_water = models.BooleanField()
    area = models.DecimalField(max_digits=5, decimal_places=2)
    heating = models.BooleanField()
    animals = models.ManyToManyField(Animal)

    def __str__(self) :
        return f'{self.name}, {self.number}'

    def get_absolute_url(self):
        return reverse('zoo:enclosure_details', args=[str(self.id)])


class CustomUser(AbstractUser):
    # employee_id = models.CharField(max_length=10, unique=True, default='not_a_staff')
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(verbose_name='email address', unique=True, max_length=244)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=30, default=)
    # last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=19, validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX',
                                   )])
    # position = models.CharField(max_length=100)
    assigned_enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)

    def employee_position(self):
        return self.assigned_enclosure.number

    def employee_first_name(self):
        return self.user.first_name

    def employee_last_name(self):
        return self.user.last_name

    def __str__(self):
        return f'{self.employee_first_name()}, {self.employee_last_name()}'
