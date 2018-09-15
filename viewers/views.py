from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from .forms import (
	UserCreationForm, 
	UserLoginForm, 
	EditProfileForm,
	UserProfileForm,
	)
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import UserProfile


# Registration
def signup(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user_auth = authenticate(username=username, password=password)
		login(request, user_auth)
		return HttpResponseRedirect('/accounts/additional_inform/{}/'.format(username))
	args = {
		'form': form
	}
	return render(request, 'accounts/sign_up.html', args)


#Login User
def login_user(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj = form.cleaned_data.get('user_obj')
		print(user_obj)
		login(request, user_obj)
		return HttpResponseRedirect('/accounts/profile')
	return render(request, 'accounts/login.html', {'form': form})


#Additional information about User
@login_required
def additional_inform(request, username):
	user = User.objects.get(username=username)

	ProfileInlineFormset = inlineformset_factory(
			User,
	 		UserProfile, 
	 		fields=
	 			[
	 			'status',
	 			'place_work',
	 			'city',
	 			'phone',
	 			'marital_status',
	 			'information',
	 			'avatar'
	 		]
	 	)
	formset = ProfileInlineFormset(instance=user)

	if request.user.is_authenticated and request.user.username  == user.username:
		if request.method == 'POST':
			formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

			if formset.is_valid():
				formset.save()
				return HttpResponseRedirect('/accounts/profile/')

		return render(request, 'accounts/account_update.html', {
        		'formset': formset
        	})
	else:
		HttpResponseRedirect('/accounts/login/')

# Adding user profile photo
'''
@login_required
def profile_photo(request, username):
	user = User.objects.get(username=username)

	if request.method == 'POST':
		form = ProfilePhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/profile/{}/'.format(user.username))
	else:
		form = ProfilePhotoForm()
	return render(request, 'accounts/avatar.html', {'form': form})
'''

def profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)


#You can change user's information
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
