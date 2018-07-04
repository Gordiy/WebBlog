from django import forms
from django.forms import ModelForm
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import MyUser
from wall.models import WallImages, MartialStatus
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()

class UserCreationForm(forms.ModelForm):
	status = forms.CharField(max_length=50)
	palace_work = forms.CharField(max_length=50)
	information = forms.CharField(widget=forms.Textarea)
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta: 
		model = User
		fields = [
			'username', 
			'first_name', 
			'last_name', 
			'email',
			]

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password do not match.')
		return password2


	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user


class UserLoginForm(forms.Form):
	query = forms.CharField(label='Username / Email')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)


	def clean(self, *args, **kwargs):
		query = self.cleaned_data.get('query')
		password = self.cleaned_data.get('password')
		user_qs_final = User.objects.filter(
				Q(username__iexact=query)|
				Q(email__iexact=query)
			).distinct()
		if not user_qs_final.exists() and user_qs_final.count != 1:
			raise forms.ValidationError("Invalid credentials - user does not exist")
		user_obj = user_qs_final.first()
		if not user_obj.check_password(password):
			raise forms.ValidationError('Credentials are not correct')
		self.cleaned_data['user_obj'] = user_obj
		return super(UserLoginForm, self).clean(*args, **kwargs)


class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
				'email',
				'first_name',
				'last_name',
				'password'
			)

