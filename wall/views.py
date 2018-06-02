from django.shortcuts import render
from django.http import Http404
from .models import WallInformation, SocialNetworks
from posts.models import Posts


def wall_information(request): 
	images = Posts.objects.all()
	social_networks = SocialNetworks.objects.filter(is_active=True)
	wall_information = WallInformation.objects.order_by('id')[0:1].get()
	return render(request, 'wall/wall.html', locals())
