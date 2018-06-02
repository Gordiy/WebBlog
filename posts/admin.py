from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
	list_display = ['id' ,'image', 'name', 'description', 'is_active', 'created', 'updated']

	class Meta:
		model = Posts

admin.site.register(Posts, PostsAdmin)
