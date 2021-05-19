from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
from userapp.models import Profile


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()

   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = "Your password must contain atleast 8 character. "
        self.fields["email"].help_text = "Please enter your email id. "
      
        # self.fields["username"].widget.attrs["placeholder"] = "Username"
        

class User_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"