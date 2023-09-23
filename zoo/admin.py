from django.contrib import admin
from .models import *

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_date', 'birth_year', 'photo', 'facts')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition')

class FoodConsumptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'animal', 'food', 'date', 'daily_amount')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_first_name', 'employee_last_name', 'phone_number', 'position')

class EnclosureAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'has_water', 'area', 'heating')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'password', 'birth_date')

class AnimalSpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class AnimalClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class HabitatCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publication_date')

class JobVacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'publication_date')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'grade')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'expiration_date', 'image')



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

admin.site.register(News, NewsAdmin)
admin.site.register(JobVacancy, JobVacancyAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Coupon,CouponAdmin)
