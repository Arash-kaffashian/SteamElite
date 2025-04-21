from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

from user.models import Account


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['steam_id']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())