from django import forms 
from bmiapp.models import Calculator

class BMIform(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = "__all__"
        exclude = ("result","user")


    