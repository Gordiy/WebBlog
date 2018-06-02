from django.db import models


class Posts(models.Model):
	id = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to='post_images/')
	name = models.CharField(max_length=36, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "{}".format(self.name)


	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
