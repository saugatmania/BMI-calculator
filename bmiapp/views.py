from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from bmiapp.forms import BMIform
from bmiapp.models import Calculator
from django.contrib.auth.decorators import login_required  
from django.core.mail import send_mail  

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
            message = "Underweight. You need to increase your weight"
        elif bmi >= 18.6 and bmi <=24.9 :
            message = "Normal weight. You are fit and fine keep it up"
        elif bmi > 25 and bmi < 29.9:
            message = "Overweight. You need to reduce your weight"
        else:
            message = "obsessed. You are very overweight, please consult a doctor"
    context = {"form": form, "bmi": bmi, "is_form_calculated": is_form_calculated, "message":message}
    return render(request, "bmi_list.html", context)


# def calculator_edit(request, id):
#     calculator = get_object_or_404 (Calculator, id=id)
#     form = BMIform(request.POST or None, instance=calculator)
#     if form.is_valid():
#         form.save() 
#         return HttpResponseRedirect(reverse("calculator:calculator_list"))
#     context = {"form":form}
#     return render(request, "bmi_list.html", context)


def calculator_delete(request, id):
    calculator = get_object_or_404(Calculator, id=id)
    calculator.delete()
    return HttpResponseRedirect(reverse("calculator:calculator_list"))


def send_report(request):
    bmi = round(Calculator.bmi(Calculator.objects.all().last()),2)
    if bmi <= 18.5:
        message = "Underweight. You need to increase your weight"
    elif bmi >= 18.6 and bmi <=24.9:
        message = "Normal weight. You are fit and fine keep it up"
    elif bmi > 25 and bmi < 29.9:
        message = "Overweight. You need to reduce your weight"
    else:
        message = "obsessed. You are very overweight, please consult a doctor"
    send_mail(  "BMI report",
                 message + " Your BMI is "+ str(bmi),
                "ytddash@gmail.com",
                [request.user.profile.email],
                # false_silently = False
            )
    
    return render(request, "report.html",{})

 