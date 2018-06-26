from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
        	'username', 
        	'first_name',
        	'last_name',
        	'email',
        	'password1', 
        	'password2', 
        	)

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.save()
		return user

