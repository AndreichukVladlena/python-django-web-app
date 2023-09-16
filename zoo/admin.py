from django.contrib import admin
from .models import *

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'class_name', 'entry_date', 'birth_year', 'photo', 'facts')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'specie')

class FoodConsumptionAdmin(admin.ModelAdmin):
    list_display = ('animal', 'food', 'date', 'daily_amount')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_first_name', 'employee_last_name', 'phone_number', 'employee_position', 'assigned_enclosure')

class EnclosureAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'has_water', 'area', 'heating')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'password')


admin.site.register(Animal, AnimalAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodConsumption, FoodConsumptionAdmin)
admin.site.register(Enclosure, EnclosureAdmin)
admin.site.register(Employee, EmployeeAdmin)