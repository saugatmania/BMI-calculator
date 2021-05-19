from django.contrib import admin
from userapp.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=("user","full_name","contact","age","gender","email","address")
