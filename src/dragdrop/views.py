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

# scaling django by using caching for scaling
from django.views.decorators.cache import cache_page

# That will allow that view to be cached for 60 minutes (60 seconds * 60 minutes).
# @cache_page(60 * 60)
# @cache_page(60)
def DraggingAndDropping(request):
    # this if statement uses a HttpRequest.method, POST - submits data to be
    # processed to a specified resource 
    if request.method == 'POST':
        user_session = Session.objects.get(pk=request.session._session_key)
        session_var = Session.objects.get(pk=request.session._session_key).get_decoded()
        user = User.objects.get(id = session_var['_auth_user_id'])
        form = UploadFileForm(request.POST, request.FILES, user)

        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.user = request.user
            new_file.save()
            return HttpResponseRedirect(reverse('dragdrop:DraggingAndDropping'))
    else:
        print "else: executed"
        form = UploadFileForm()

    data = {'form': form}
    return render_to_response('dropzone-drag-drop.html', data, context_instance=RequestContext(request))


# @cache_page(60)
def GetUserImages(request):
    all_images = UploadFile.objects.all().filter(user_id=request.user.id)
    this_context = {
        'images': all_images,
        'user': request.user
    }
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

