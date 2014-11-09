from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
# are a way to tell the database what data to store
# "solid-state data" concept

# define our SignUp model
# singular class
class SignUp(models.Model):
    
    # a character field that takes a max length of 120 characters it can also be blank in the data base and also blank in the form or template being added to       
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    # null=False is because that their needs to be a require e-mail in the database, when someone signs up
    email = models.EmailField(null=False, blank=False)
    
    # timestamps will be automatic and won't actually show up on the Django administration signup page
    # auto_now_add, when its created create a timestamp. We want a 1 time update when the user first inputs e-mail
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated time, which is the reverse logic of timestamp
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    # for special foreign users with special characters/accents
    def __unicode__(self):
        # self.email the instance we inputed when we are signing-up on our Django admin page
        return smart_unicode(self.email)
        # return "some unicode" <--This hack can change the email names on the admin page

