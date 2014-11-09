from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from drinker.files import get_upload_path

class Drinker(models.Model):
	user    = models.OneToOneField(User)
	# user    = models.ForeignKey(User, unique=True)
	# user    = models.ForeignKey(User)
	name    = models.CharField(max_length=100)
	file    = models.FileField(upload_to=get_upload_path)

	def __unicode__(self):
		return self.name
