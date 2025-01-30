from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import CustomUser

class UserRegFrm(UserCreationForm):
    username=forms.CharField(
        label=("Enter Username"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    first_name=forms.CharField(
        label=("First Name"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name=forms.CharField(
        label=("Last Name"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email=forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    mobile=forms.CharField(
        label=("Mobile Number"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','mobile')

class UserLogFrm(AuthenticationForm):
    username=forms.CharField(
        label=("Enter Username"),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password=forms.CharField(
        label=("Enter Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
