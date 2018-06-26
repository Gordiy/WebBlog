from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from viewers.forms import SignUpForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
        	form.save()
        	username = request.user
        	return redirect('/accounts/profile/')
        	login(request, user)
    else:
        form =  SignUpForm()
        args = {'form': form}
        return render(request, 'accounts/sign_up.html', args )
    return render(request, 'accounts/sign_up.html', {'form': form})


def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.user
			
			print(str(username))
			return redirect('/accounts/profile/')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})


def profile(request, username):
	user_profile = User.objects.get(username=username)
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)

