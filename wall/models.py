from django.db import models


class SocialNetworks(models.Model):
	name = models.CharField(max_length=36, blank=True, null=True, default=None)
	link = models.CharField(max_length=58, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return "{}".format(self.link)

	class Meta: 
		verbose_name = "Social Network"
		verbose_name_plural = "Social Networks"


class MartialStatus(models.Model):
	status = models.CharField(max_length=36, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return "{}".format(self.status)


	class Meta:
		verbose_name = 'Martial status'
		verbose_name_plural = 'Martial statuses'

class WallImages(models.Model):
	image = models.ImageField(upload_to='wall_images/')
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	class Meta:
		verbose_name = 'Wall Image'
		verbose_name_plural = 'Wall Images'


class WallInformation(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=36, blank=True, null=True, default=None)
	last_name = models.CharField(max_length=36, blank=True, null=True, default=None)
	status = models.CharField(max_length=85, blank=True, null=True, default=None)
	place_work = models.CharField(max_length=36, blank=True, null=True, default=None)
	marital_status = models.ForeignKey(MartialStatus, blank=True, on_delete=models.CASCADE, null=True, default=None)
	information = models.TextField(blank=True, null=True, default=None)
	image = models.ForeignKey(WallImages, blank=True, on_delete=models.CASCADE, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "{}".format(self.last_name)


	class Meta:
		verbose_name = 'Wall Information'
		verbose_name_plural = 'Wall Information'


