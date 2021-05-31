from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'phone', 'description']