from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from .forms import (
	UserCreationForm, 
	UserLoginForm, 
	EditProfileForm,
	)
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash


def signup(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect('/accounts/login')
	args = {
		'form': form
	}
	return render(request, 'accounts/sign_up.html', args)


def login_user(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj = form.cleaned_data.get('user_obj')
		print(user_obj)
		login(request, user_obj)
		return HttpResponseRedirect('/accounts/profile')
	return render(request, 'accounts/login.html', {'form': form})


def profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)


def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/profile')
		else:
			return HttpResponseRedirect('/accounts/profile/password/')

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)
