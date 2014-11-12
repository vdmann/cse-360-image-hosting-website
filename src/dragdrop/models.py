from django.db import models
from dragdrop.files import get_path
from django.contrib.auth.models import User
from drinker.models import Drinker
from django.conf import settings

# Create your models here.
def _upload_path(instance, filename):
	return instance.get_upload_path(filename)

# this gets the user (hardcoded)
# u = User.objects.get(pk=2) # Get the first user in the system
# user_address = u.get_profile().home_address

class UploadFile(models.Model):
	file = models.ImageField(upload_to=_upload_path)
	# file = models.FileField(upload_to='file/%Y/%m/%d')
	# user = models.ForeignKey('auth.User')
	user = models.ForeignKey(User)
	# user = models.ForeignKey(Drinker)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL)
	# user = models.ForeignKey(Drinker, related_name="")		
	# user = models.ForeignKey(User, unique=True)
	# user = models.ForeignKey(User, null=True, blank=True)
	# user = models.OneToOneField(User)

	def get_upload_path(self, filename):
		return "user_"+str(self.user.username)+"/"+filename


# when user = models.ForeignKey(User) is not commented
#
# form: <tr><th><label for="file">File:</label></th><td><input id="file" name="file" type="file" /></td></tr>
# <tr><th><label for="user">User:</label></th><td><ul class="errorlist"><li>This field is required.</li></ul><select id="user" name="user">
# <option value="" selected="selected">---------</option>
# <option value="1">dee-mann</option>
# </select></td></tr> 
# 
# 
# 
# this form did not process form.is_valid() line, there is an error validating data
# 
# 
# <ul class="errorlist"><li>user<ul class="errorlist"><li>This field is required.</li></ul></li></ul>




# successful with the user = models.ForeignKey(User) commented
# 
# form: <tr><th><label for="file">File:</label></th><td><input id="file" name="file" type="file" /></td></tr>
# <tr><th><label for="user">User:</label></th><td><select id="user" name="user">
# <option value="" selected="selected">---------</option>
# <option value="1">dee-mann</option>
# </select></td></tr> 
# 
# 
# 
# if form.is_valid(): executed
# 
# 
# True