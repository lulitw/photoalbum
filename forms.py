from django import forms
from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class MAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'span2','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'span2','placeholder':'Password'}))

class MUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'span2','placeholder': 'Username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'span2','placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'span2','placeholder':'Confirm Password'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'span2','placeholder': 'Email'}))

