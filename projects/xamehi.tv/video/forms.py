from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Movies, Profile, Series


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class MoviesForm(ModelForm):

    class Meta:
        model = Movies
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class SeriesForm(ModelForm):

    class Meta:
        model = Series
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Movies, Profile, Series


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class MoviesForm(ModelForm):

    class Meta:
        model = Movies
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class SeriesForm(ModelForm):

    class Meta:
        model = Series
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
