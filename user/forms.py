from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import *

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserModel
        fields = ['name','username', 'second_name', 'email', 'password', 'customer']

class LoginForm(AuthenticationForm):
    pass

# class UserDeleteForm(UserChangeForm):
#     class Meta:
#         model = UserModel
#         fields = "__all__"

