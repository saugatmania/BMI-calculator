from django.contrib import admin
from bmiapp.models import Calculator

@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display=("weight","height","bmi","created","modified")

