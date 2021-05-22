from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http  import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from userapp.forms import CustomSignupForm, User_profile
from userapp.models import Profile
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import logout

   

def user_profile(request):
    list = Profile.objects.filter(user=request.user)
    context = {"list":list}
    return render(request, "user_profile.html",context)


def my_profile(request):
    pro = Profile.objects.filter(user=request.user)
    context={"list":pro}
    return render (request, "bmi_list.html", context)


class UserLogin(LoginView):
    template_name = "user_login.html"
    redirect_authenticated_user = False


def profile_create(request):
    form = User_profile(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("userapp:profile"))
    context = {"form":form}
    return render(request, "profile_create.html", context)


def signup_view(request):
    form = CustomSignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("userapp:user_login"))
    context = {"form": form}
    return render(request, "register.html", context)


def profile_edit(request, id):
    profile = get_object_or_404 (Profile, id=id)
    form = User_profile(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("userapp:profile"))
    context = {"form":form}
    return render(request, "profile_create.html", context)


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect("/user/login/")


def send_confirm_email(request):
    subject = "Test Subject"
    message = "Test Meassage"
    from_email = "ytddash@gmail.com"
    recipient_list = ["saugatbasnet5@gmail.com"]
    context = {"name": "Saugat"}      
    html_message = render_to_string("user_profile.html")
    res = send_mail(subject, message, from_email,
                    recipient_list, html_message=html_message)
    return HttpResponse(res)