from django.urls import path
from bmiapp.views import calculator_list, calculator_add, calculator_edit, calculator_delete, suggestion_show

app_name = "calculator"

urlpatterns = [
    path("calculator-list/", calculator_list, name = "calculator_list"),
    path("calculator-add/", calculator_add, name = "calculator_add"),
    path("calculator-edit/<int:id>/", calculator_edit, name = "calculator_edit"),
    path("calculator-delete/<int:id>/", calculator_delete, name="calculator_delete"),
    path("suggestion-show/", suggestion_show, name = "suggestion_show"),
]


