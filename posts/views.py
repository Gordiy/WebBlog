from django.shortcuts import render
from .models import Posts
from wall.models import WallInformation
from django.http import Http404


def posts(request):
	try:
		posts = Posts.objects.filter(is_active=True)
	except Posts.DoesNotExist:
		raise Http404("Any post are not created ")


	wall_information = WallInformation.objects.order_by('id')[0:1].get()
	return render(request, 'posts/posts.html', locals())
