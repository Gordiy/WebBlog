from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm
from .models import MyUser

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = (
		'id',
		'username', 
		'email', 
		'first_name', 
		'last_name',  
		'is_admin')
	list_filter = ('is_admin',)

	fieldsets = (
			(None, {'fields': (
				'username', 
				'email', 
				'password',
				'first_name', 
				'last_name', 
				'status', 
				'place_work', 
				'information',
				'avatar', 
				'is_admin'
				)}),
			('Premission', {'fields': ('is_admin',)})
		)
	search_fields = ('username', 'email')
	ordering = ('username', 'email')

	filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)


admin.site.unregister(Group)
