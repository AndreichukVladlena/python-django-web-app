from django.contrib import admin
from .models import *

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'animal_class', 'entry_date', 'birth_year', 'photo', 'facts')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition')

class FoodConsumptionAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'animal', 'food', 'date', 'daily_amount')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_first_name', 'employee_last_name', 'phone_number', 'assigned_enclosure', 'position')

class EnclosureAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'has_water', 'area', 'heating')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'password')

class AnimalSpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class AnimalClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class HabitatCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')



admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalSpecies, AnimalSpeciesAdmin)
admin.site.register(AnimalClass, AnimalClassAdmin)
admin.site.register(HabitatCountry, HabitatCountryAdmin)
admin.site.register(EmployeePosition, EmployeePositionAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodConsumption, FoodConsumptionAdmin)
admin.site.register(Enclosure, EnclosureAdmin)
admin.site.register(Employee, EmployeeAdmin)