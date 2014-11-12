from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User 
from django.db import models
from django.template import Context, Template
from django.conf import settings
from .forms import UploadFileForm
from .models import UploadFile

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

        # user_print_test_in = models.IntegerField(User)
        user_print_test = models.ForeignKey(User, unique=True)
        print "this is the user_print_test value: %s" % user_print_test


        ########################################################################
        # request.FILES is passed into the constructor UploadFileForm; this is 
        # how file data gets bound into a form
        # 
        # This view handling the form will receive the file data in 
        # request.FILES, which is a dictionary containing a key for each 
        # FileField (or ImageField, or other FileField subclass) in the form. 
        # So the data from the above form would be accessible as 
        # request.FILES['file'].
        # 
        # Note that request.FILES will only contain data if the request method 
        # was POST and the that posted the request has the attribute 
        # enctype= multipart/form-data . Otherwise, request.FILES will be empty.
        # ###################################################################### 
        
        # why are we passing user into UploadFileForm?
        # form = UploadFileForm(request.POST, request.FILES, user)
        # form = UploadFileForm(request.POST, request.FILES, request.user)

        print "\n\n"
        # print "form: %s " % form
        print "the value of request.POST: %s" % request.POST
        print "the value of request.FILES: %s" % request.FILES

        print "before assigning form: %s" % UploadFileForm(request.POST, request.FILES)
        


    
        # this works by default without the user session id
        form = UploadFileForm(request.POST, request.FILES, user)

        ########################################################################

        if form.is_valid():

            # test print statement 
            print "\n\n"
            print "if form.is_valid(): executed"
            print "\n"
            print form.is_valid()
            print "\n\n"


            new_file = UploadFile(file = request.FILES['file'])
            
            print "\n"
            print "request.user: %s" % request.user

            new_file.user = request.user

            print "\n"
            print "new_file.user: %s" % new_file.user
            print "\n"

            print "this is the user printed within dragdrop: %s" % user
            print "new_file.user = request.user value: %s" % new_file.user
            
            new_file.save()

            # THIS IS FROM drinker views.py 
            # 
            # creates the user object with the attributes from form by passing it the input from POST
            # user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            # save the user object, which provides the user the ability to log in
            # user.save()
            # drinker = Drinker(user=user, name=form.cleaned_data['name'])
            # drinker.save()

            return HttpResponseRedirect(reverse('dragdrop:DraggingAndDropping'))

        # this is a test statement
        if form.errors:
            print "\n\n"
            print "this form did not process form.is_valid() line, there is an error validating data"
            print "\n"
            print form.errors
            print "\n\n"


    else:
        print "else: executed"
        form = UploadFileForm()
 
    print "after conditional statements"
    


    # ########################################################################
    # # TA's code
    # # debugging statment 
    # user_session = Session.objects.get(pk=request.session._session_key)
    # # print "in views.py is the user id: %s" % user_session.get_decoded()
    # # remember that the session key is a string so the id number has to be
    # # converted in to an integer
    # session_var = Session.objects.get(pk=request.session._session_key).get_decoded()
    
    # user = User.objects.get(id = session_var['_auth_user_id'])
    # # print "this is the user string: %s" % user

    # user_print_test = models.ForeignKey(User, unique=True)
    # # print "this is the user_print_test value: %s" % user_print_test
    # ########################################################################

    # ########################################
    # # printing tests for filtering
    all_images = UploadFile.objects.all().filter(user_id=request.user.id)
    # # all_images = UploadFile.objects.all().filter(id)    
    print all_images
    # ########################################
 


    # this has global access for the entire website
    data = {'form': form}
    return render_to_response('dropzone-drag-drop.html', data, context_instance=RequestContext(request))
   
    # pictures = UploadFile.objects.all()
    # return render_to_response('index.html', {'pictures': pictures, 'form': form}, context_instance=RequestContext(request))



def GetUserImages(request):

    # not sure if this works with Dropzone UploadFile class model 
    # ok so this actually works for all the images stored into the database 
    # not for each unique user with a unique amount of pictures
    # 
    #  all_images = UploadFile.objects.all()
    # 
    # so what we need to do is apply a filter
    # print "\n\n\n\nThis is in GetUserImages python function"
    # print "this is the user_id value: %s" request.user.id
    # print "this is the file from the user: %s " % request.user.file
    all_images = UploadFile.objects.all().filter(user_id=request.user.id)
    # user_images = User.objects.get(pk=all_images['id_file'])
    print "these are all_images: %s" % all_images

    # Python dictionaries are also known as associative arrays or hash tables. 
    # The general syntax of a dictionary is as follows:
    this_context = {
        'images': all_images,
        'user': request.user
    }

    # arugments
    return render_to_response('index.html', this_context, context_instance=RequestContext(request))


################################################################################
# import os
# import glob
# import fnmatch, re
# from django.conf import settings

# def GetUserImages2(request):
    
#     image_string = str(glob.glob("*.jpg"))
#     base_dir_path = settings.BASE_DIR
#     img_list = os.path.join(os.path.dirname(base_dir_path),
#         "static", "media", "user_"+request.user.username+"/"+image_string)  

#     return render_to_response('index.html', {'images': img_list})
################################################################################

