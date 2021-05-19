from django import forms 
from bmiapp.models import Calculator, Suggestion

class BMIform(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = "__all__"
        exclude = ("result","user")

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = "__all__"
    