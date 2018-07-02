from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect


def signup(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
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

