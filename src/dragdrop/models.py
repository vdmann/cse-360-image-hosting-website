from django.db import models
from dragdrop.files import get_path
from django.contrib.auth.models import User
from drinker.models import Drinker

def _upload_path(instance, filename):
	return instance.get_upload_path(filename)

# Create your models here.
class UploadFile(models.Model):
	file = models.ImageField(upload_to=_upload_path)
	# file = models.FileField(upload_to='file/%Y/%m/%d')
	# user = models.ForeignKey('auth.User')
	# user = models.ForeignKey(User)
	# user = models.ForeignKey(Drinker, related_name='images')		
	# user = models.ForeignKey(User, unique=True)
	user = models.ForeignKey(User, null=True, blank=True)	

	def get_upload_path(self, filename):
		return "user_"+str(self.user.username)+"/"+filename
