from django.contrib import admin
from bmiapp.models import Calculator, Suggestion

@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display=("weight","height","bmi","created","modified")

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display=("suggestion",)