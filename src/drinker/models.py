from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from drinker.files import get_upload_path

# # user profile avatar
# def _upload_path(instance, filename):
# 	return instance.get_upload_path(filename)

class Drinker(models.Model):
	user    = models.OneToOneField(User)
	name    = models.CharField(max_length=100)
	# user profile avatar
	# upload_to= "insert dynamic upload files here"
	# avatar 	= models.ImageField("Profile Picture", upload_to=_upload_path, blank=True, null=True)

    # user profile avatar
	# def get_upload_path(self, filename):
	# 	return "user_"+str(self.user.username)+"/"+filename

	def __unicode__(self):
		return self.name
