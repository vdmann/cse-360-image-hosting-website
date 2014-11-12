from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models

# am I importing these session libraries correctly?
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.cached_db import SessionStore
from django.contrib.sessions.backends.db import SessionStore

from django.conf import settings
import random, string
from importlib import import_module



def get_path(instance, filename):
    
    ctype = ContentType.objects.get_for_model(instance)
    model = ctype.model
    app = ctype.app_label
    extension = filename.split('.')[-1]

    ############################################################################
    # string for the session id
    # s = request.session._session_key
    # request.user.username

    # user_print_test = models.IntegerField(User)
    # user_print_test = models.ForeignKey(User, unique=True)
    # print "in files.py this is the user_print_test value: %s" % user_print_test
    #  using session outside of the views  
    # SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
    # this randomly creates a sessionid everytime 
    # s = SessionStore()
    # s.save()
    # s.session_key
    # print "in files.py this is the s.session_key value: %s" % s.session_key
    # get_session_key = s.session_key
    # session_var = Session.objects.get(pk=s.session_key).get_decoded()
    # print "in files.py this is the s.session_var value: %s" % session_var

    # this does not work
    # user_get_id = User.objects.get(id = session_var['_auth_user_id'])
    # print "this is the session_key value: %s" % user_get_id
    ############################################################################

    # modified code
    # dir = get_session_key
    
    # original code 
    dir = "site"

    # if model == "job":
    #     dir += "/pdf/job_attachment"
    # else:
    #     dir += "/img/%s" % app
    #     if model == "image_type_1":
    #         dir += "/type1/%s" % instance.category
    #     elif model == "image_type_2":
    #         dir += "/type2"
    #     elif model == "restaurant":
    #         dir += "/logo"
    #     else:
    #         dir += "/%s" % model

    
    chars = string.letters + string.digits
    name = string.join(random.sample(chars, 8), '')
   
    #  original code
    # return "%s/%s/%s.%s" % (dir, name, extension)
    
    return "%s/%s.%s" % (dir, filename, extension)