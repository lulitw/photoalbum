from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.forms import AuthenticationForm
from albumr.models import Album, Page, PageItem


class AlbumForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Album Name'} ))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Album Description'} ))

    class Meta:
        model = Album

        exclude = ('owner', 'created', 'unique_url')


class AlbumAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'span2','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'span2','placeholder':'Password'}))