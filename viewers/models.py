from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from wall.models import WallImages, MartialStatus


class MyUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError('Users must have an email address.')

		user = self.model(username=username, email=normalize_email(email))
		user.set_password(password)
		user.save(using=self._db)
		return user

class MyUser(AbstractBaseUser):
	id = models.AutoField(primary_key=True)
	username =  models.CharField(max_length=300, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
	status = models.CharField(max_length=85, blank=True, null=True, default=None)
	place_work = models.CharField(max_length=36, blank=True, null=True, default=None)
	marital_status = models.ForeignKey(MartialStatus, blank=True, on_delete=models.CASCADE, null=True, default=None)
	information = models.TextField(blank=True, null=True, default=None)
	avatar = models.ForeignKey(WallImages, blank=True, on_delete=models.CASCADE, null=True, default=None)
	is_admin = models.BooleanField(default=False)
	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']


	def has_perm(self, perf, obj=None):
		return True


	def has_module_perms(self, app_label):
		return True


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=85, blank=True, null=True, default=None)
	place_work = models.CharField(max_length=36, blank=True, null=True, default=None)
	city=models.CharField(max_length=100, default='')
	phone = models.IntegerField(default=12)
	marital_status = models.ForeignKey(MartialStatus, blank=True, on_delete=models.CASCADE, null=True, default=None)
	information = models.TextField(blank=True, null=True, default=None)

	def __str__(self):
		return self.user.username

def create_profile(sender,**kwargs ):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
		