from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .models import UserProfile


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account for {username} was created successfully! You can now log in')
			return redirect('user-login')
	else:
		form = UserRegisterForm()
	return render(request, 'registration.html', {'form': form, 'title': 'Registration'})


@login_required
def redirector(request):
	return redirect('user-profile', request.user.username)


class UserProfileView(UpdateView):
	model = UserProfile
	fields = ['bio',]
	slug_field = 'username'
	template_name = 'profile.html'
	context_object_name = 'User'

class UserProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = UserProfile
	fields = [
		'avatar',
		'first_name',
		'last_name',
		'email',
		'title',
		'course',
		'level',
		'country',
		'icon',
		'instagram',
		'facebook',
		'telegram',
		'twitter',
	]
	slug_field = 'username'
	template_name = 'profile_edit.html'
	context_object_name = 'User'

	def test_func(self):
		profile = self.get_object()

		if self.request.user.username == profile.username:
			return True
		return False
