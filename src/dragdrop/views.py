from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User 
from django.db import models
# this is used to create template tag objects
from django.template import Context, Template
# from django import forms <--- Do I need this?
from django.conf import settings


# from within dragdrop
from .forms import UploadFileForm
from .models import UploadFile
# from drinker.forms import UploadFileForm
# from drinker.models import UploadFile
# import os
# from django.conf import settings
# from annoying.decorators import ajax_request

# from django.db.models import get_model


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




################################################################################
# # this is for displaying the images. So, what we want to do in this function is
# # to create a template tag for our list of images in the views this means from
# # our models.py file using the class UploadFile we can get all the images that
# # are uploaded concurrently by doing UploadFile.objects.all. But I think a
# # better way to approach this is to use UploadFile.objects.user.all() <--- which
# # im not sure if this is possible. Since we are uploading each image
# # individually we are essentially creating an association between the user and 
# # the images that are uploaded to the database
# # 
# # what I'm thinking is that UploadFile.objects.all gets all the image within the
# # instance that the user has already uploaded their image file
# # def GetUserImages(request, template='index.html'):

def GetUserImages2(request):

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
    }

    # this is a test
    # this_template = template.Template{'My template images {{ images }}.'}
    # this_context = template.Context{'images': all_images,}


    # figure out what RequestContext does, and how render_to_response takes its
    # arugments
    return render_to_response('index.html', this_context, context_instance=RequestContext(request))
################################################################################


################################################################################
import os
import glob
import fnmatch, re
from django.conf import settings

def GetUserImages(request):
    
    # path="static/media/user_dee-mann"  # insert the path to your directory   

    image_string = str(glob.glob("*.jpg"))
    base_dir_path = settings.BASE_DIR
    img_list = os.path.join(os.path.dirname(base_dir_path),
        "static", "media", "user_"+request.user.username+"/"+image_string)  
    
    # print "\n\n\n\nThis is using glob in GetUserImages" 
    # print "this image_string value: %s" % image_string
    # img_list = "user_"+request.user.username

    return render_to_response('index.html', {'images': img_list})
################################################################################





################################################################################


# this is the path to the links work for static and media
# ^static\/(?P<path>.*)$
# ^media\/(?P<path>.*)$

################################################################################
# def template_user_images():
#     bits = token.split_contents()
################################################################################


    

################################################################################
# import os
# from django.conf import settings
# from annoying.decorators import ajax_request

# @ajax_request
# def json_images(request, dir_name):
#     path = os.path.join(settings.MEDIA_ROOT, dir_name)
#     images = []
#     for f in os.listdir(path):
#         if f.endswith("jpg") or f.endswith("png"): # to avoid other files
#             images.append("%s%s/%s" % (settings.MEDIA_URL, dir_name, f)) # modify the concatenation to fit your neet
#     return {'images': images}

################################################################################




################################################################################
# views.py

# import os 

# def gallery(request):
#     path="C:\\somedirectory"  # insert the path to your directory   
#     img_list =os.listdir(path)   
#     return render_to_response('gallery.html', {'images': img_list})

# gallery.html

# {% for image in images %}
# <img src='/static/{{image}}' />
# {% endfor %}
################################################################################






################################################################################
# writting your own template tags
# 
# Start off by creating a folder called templatetags in your app directory and 
# create two files in it. The first one named __init__.py and the second 
# book tags.py. Theres 3 things that we need to accomplish with our template 
# tags. The first is to create a tag that will output the url for the action of 
# the form. For example, {% get_book_form_url foo_object %}Next we need to get 
# the form and assign it to a template variable that can be specified by the 
# template variable. For example, {% book_form as bar_var %}. And the third 
# template tag will get the books for an object and place in a template 
# variable. For example, {% books_for_object foo_object as bar_var %}.
# 
# 
# from django.template import Library, Node, TemplateSyntaxError
# from django.template import Variable, resolve_variable
# from django.utils.translation import ugettext as _
# from django.contrib.contenttypes.models import ContentType
# from django.core.urlresolvers import reverse
# from books.models import Book
 
# register = Library()
 
# def get_contenttype_kwargs(content_object):
#     """
#     Gets the basic kwargs necessary for form submission url
#     """
#     kwargs = {'content_type_id':
#         ContentType.objects.get_for_model(content_object).id,
#     'object_id':
#         getattr(content_object, 'pk',
#             getattr(content_object, 'id')),
#     }
#     return kwargs
 
# def get_book_form_url(content_object):
#     """
#     prints url for form action
#     """
#     kwargs = get_contenttype_kwargs(content_object)
#     return reverse('new_book', kwargs=kwargs)
 
# class BooksForObjectsNode(Node):
#     """
#     Get the books and add to the context
#     """
#     def __init__(self, obj, context_var):
#         self.obj = Variable(obj)
#         self.context_var = context_var
 
#     def render(self, context):
#         content_type = ContentType.objects.get_for_model(
#             self.obj.resolve(context))
#         # create the template var by adding to context
#         context[self.context_var] = \
#             Book.objects.filter( # find all books for object
#                 content_type__pk = content_type.id,
#                 object_id = self.obj.resolve(context).id
#             )
#         return ''

# # why is this custom template tag written in python taking a parser and token
# # argument?
# def books_for_object(parser, token):
#     """
#     Retrieves a list of books for given object
#     {% books_for_object foo_object as book_list %}
#     """
#     try:
#         bits = token.split_contents()
#     except ValueError:
#         raise TemplateSyntaxError(
#             _('tag requires exactly two arguments')
#     if len(bits) != 4:
#         raise TemplateSyntaxError(
#             _('tag requires exactly three arguments')
#     if bits[2] != 'as':
#         raise TemplateSyntaxError(
#             _("second argument to tag must be 'as'")
#     return BooksForObjectsNode(bits[1], bits[3])
 
# def book_form(parser, token):
#     """
#     Adds a form to the context as given variable
#     {% book_form as form %}
#     """
#     # take steps to ensure template var was formatted properly
#     try:
#         bits = token.split_contents()
#     except ValueError:
#         raise TemplateSyntaxError(
#             _('tag requires exactly two arguments')
#     if bits[1] != 'as':
#         raise TemplateSyntaxError(
#             _("second argument to tag must be 'as'")
#     if len(bits) != 3:
#         raise TemplateSyntaxError(
#             _('tag requires exactly two arguments')
#     # get the form
#     return BookFormNode(bits[2])
 
# class BookFormNode(Node):
#     """
#     Get the form and add it to the context
#     """
#     def __init__(self, context_name):
#         self.context_name = context_name
#     def render(self, context):
#         from books.forms import NewBookForm
#         form = NewBookForm()
#         # create the template var by adding to context
#         context[self.context_name] = form
#         return ''
 
# # register these tags for use in template files
# register.tag('books_for_object', books_for_object)
# register.tag('book_form', book_form)
# register.simple_tag(get_book_form_url) 
################################################################################





################################################################################
# # this is on the HTML side
# <h2>Books</h2>

# # "load"
# # 
# # Load a custom template tag set. See Chapter 9 for more information on custom 
# # template libraries.
# # 
# # what this does is basically loading the book_tags.py file with the custom tags
# # we have made
# {% load book_tags %}
 
# # so this line calls def books_for_object(parser, token): 
# {% books_for_object my_awesome_object_here as books %}
# {% for book in books %}
 
# <a href="{{ book.get_absolute_url }}">{{ book }}</a> -
#         {{ book.description }}
 
# {% endfor %}
# <h2>Add a book</h2>
# <form action="{% get_book_form_url my_awesome_object_here %}" method="post">
# {% book_form as form %}
# {{ form }}
# <input type="submit" value="Go" />
# </form>
################################################################################
