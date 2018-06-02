from django.contrib import admin
from .models import *


class WallInformationAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'status', 'place_work', 'marital_status', 'information', 'created', 'updated']

	class Meta:
		model = WallInformation

admin.site.register(WallInformation, WallInformationAdmin)


class SocialNetworksAdmin(admin.ModelAdmin):
	list_display = ['name', 'link', 'is_active']

	class Meta:
		model = SocialNetworks

admin.site.register(SocialNetworks, SocialNetworksAdmin)


class MartialStatusAdmin(admin.ModelAdmin):
	list_display = ['status', 'is_active']

	class Meta:
		model = MartialStatus

admin.site.register(MartialStatus, MartialStatusAdmin)


class WallImagesAdmin(admin.ModelAdmin):
	list_display = ['image', 'is_active', 'created', 'updated']

	class Meta:
		model = WallImages

admin.site.register(WallImages, WallImagesAdmin)