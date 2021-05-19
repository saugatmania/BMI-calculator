from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from bmiapp.forms import BMIform
from bmiapp.models import Calculator, Suggestion
from django.contrib.auth.decorators import login_required    

def calculator_list(request):
    list = Calculator.objects.filter(user=request.user)        
    context = {"list":list}
    return render(request, "calculator_list.html",context)

@login_required           
def calculator_add(request):
    bmi = None
    message = None
    is_form_calculated = False
    form = BMIform(request.POST or None, request.FILES or None)
    if form.is_valid():
        calculator = form.save(commit=False)
        calculator.user = request.user
        calculator.save()
        is_form_calculated = True
        bmi = calculator.bmi()

        if bmi <= 18.5:
            message = "Underweight"
        elif bmi >= 18.6 and bmi <=24.9 :
            message = "Normal weight"
        elif bmi > 25 and bmi < 29.9:
            message = "Overweight"
        else:
            message = "obsessed"
        # return HttpResponseRedirect(reverse("calculator:calculator_list"))
    context = {"form": form, "bmi": bmi, "is_form_calculated": is_form_calculated, "message":message}
    return render(request, "bmi_list.html", context)

def calculator_edit(request, id):
    calculator = get_object_or_404 (Calculator, id=id)
    form = BMIform(request.POST or None, instance=calculator)
    if form.is_valid():
        form.save #esko braket hatako 
        return HttpResponseRedirect(reverse("calculator:calculator_list"))
    context = {"form":form}
    return render(request, "bmi_list.html", context)


def calculator_delete(request, id):
    calculator = get_object_or_404(Calculator, id=id)
    calculator.delete()
    return HttpResponseRedirect(reverse("calculator:calculator_list"))

def suggestion_show(request):
    # list = Suggestion.objects.all()
    # context = {"list":list}
    context = {}
    if request.POST:
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))

        result = (weight/(height*height))
        if result < 18.5:
            suggestion = "underweight"
        elif result > 18.6 and result < 24.9:
            suggestion = "ideal"
        elif result > 25 and result < 29.9:
            suggestion = "overweight"
        elif result > 30: 
            suggestion = "obesity"
        
        context = suggestion
        return HttpResponseRedirect(reverse("calculator:suggestion_show"))
        context = {"bmi": bmi}
    return render (request, "suggestion_show.html",context)


 