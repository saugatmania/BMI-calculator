from django.urls import path
from userapp.views import UserLogin, signup_view, user_profile, send_confirm_email, profile_edit, profile_create , UserLogout

app_name = "userapp"

urlpatterns = [
    path("login/", UserLogin.as_view(), name = "user_login"),
    path("register/", signup_view, name="register"),
    path("profile/", user_profile, name="profile"),
    path("email/", send_confirm_email, name="send_email"),
    path("edit/<int:id>/",profile_edit, name="profile_edit"),
    path("create/", profile_create, name="profile_create"),
    path("logout/", UserLogout, name = "UserLogout"),
]