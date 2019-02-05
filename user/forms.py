from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, Status


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = UserProfile
		fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']


class StatusCreationForm(forms.ModelForm):

	class Meta:
		model = Status
		fields = ['text', 'img']


class BioUpdateForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ['bio']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


