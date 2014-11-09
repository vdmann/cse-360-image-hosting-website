from django.http import HttpResponseRedirect
from django.template import RequestContext
# why are we using reverse URL lookup?
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User 
from django.db import models
# from django import forms

# from within dragdrop
from forms import UploadFileForm
from models import UploadFile
# from drinker.forms import UploadFileForm
# from drinker.models import UploadFile
 
import os
from django.conf import settings
from annoying.decorators import ajax_request


# passes an HttpRequest through DraggingAndDropping
def DraggingAndDropping(request):
    # this if statement uses a HttpRequest.method, POST - submits data to be
    # processed to a specified resource 
    if request.method == 'POST':

        ########################################################################
        # TA's code
        # debugging statment 
        user_session = Session.objects.get(pk=request.session._session_key)
        print "in views.py is the user id: %s" % user_session.get_decoded()
        # remember that the session key is a string so the id number has to be
        # converted in to an integer
        session_var = Session.objects.get(pk=request.session._session_key).get_decoded()
        
        user = User.objects.get(id = session_var['_auth_user_id'])
        # user.save()
        # request.session.modified = True
        print "this is the user string: %s" % user

        # user_print_test = models.IntegerField(User)
        user_print_test = models.ForeignKey(User, unique=True)
        print "this is the user_print_test value: %s" % user_print_test

        # request.FILES is passed into the constructor UploadFileForm; this is 
        # how file data gets bound into a form
        # form = UploadFileForm(request.POST, request.FILES, user)

        # print "form: %s " % form
        
        # this works by default without the user session id
        form = UploadFileForm(request.POST, request.FILES)
        ########################################################################

        if form.is_valid():
            print "if form.is_valid(): executed"
            new_file = UploadFile(file = request.FILES['file'])
            
            new_file.user = request.user
            print "new_file.user = request.user value: %s" % new_file.user
            
            new_file.save()
            # not sure what this does, look into the reverse class from django.core.urlresolvers
            return HttpResponseRedirect(reverse('dragdrop:DraggingAndDropping'))
    else:
        print "else: executed"
        form = UploadFileForm()
 
    print "after conditional statements"

    # this has global access for the entire website
    data = {'form': form}
    return render_to_response('dropzone-drag-drop.html', data, context_instance=RequestContext(request))
   
    # pictures = UploadFile.objects.all()
    # return render_to_response('index.html', {'pictures': pictures, 'form': form}, context_instance=RequestContext(request))



# @ajax_request
# def json_images(request, dir_name):
#     path = os.path.join(settings.MEDIA_ROOT, dir_name)
#     images = []
#     for f in os.listdir(path):
#         if f.endswith("jpg") or f.endswith("png"): # to avoid other files
#             images.append("%s%s/%s" % (settings.MEDIA_URL, dir_name, f)) # modify the concatenation to fit your neet
#     return {'images': images}