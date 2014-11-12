from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinker.forms import RegistrationForm, LoginForm
from drinker.models import Drinker
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session


# if user hits the registration or already logged-in send them to profile since they are already registered
def DrinkerRegistration(request):
    
    if request.user.is_authenticated():
        
        ##################
        # printing the session id to a string
        request.session._session_key
        print "this is the sessionid: %s" % request.session._session_key
        ##################  
        #
        return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))

    # what happens after someone submits the form
    if request.method == 'POST':
        # take the registration form takes what evers been filled out and post it
        form = RegistrationForm(request.POST)

        # custom validation through our clean methods through our fields
        if form.is_valid():
            
            # creates the user object with the attributes from form by passing it the input from POST
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            # save the user object, which provides the user the ability to log in
            user.save()
            drinker = Drinker(user=user, name=form.cleaned_data['name'])
            drinker.save()
           
            ##################
            # printing the session id to a string
            request.session._session_key
            print "this is the sessionid: %s" % request.session._session_key
            ##################  
            
            return HttpResponseRedirect('/login/')

        # incase the form does not validate, when the user's are taken and passwords do not match, or email is invalid
        else:

            ##################
            # printing the session id to a string    
            request.session._session_key
            print "this is the sessionid: %s" % request.session._session_key
            ##################  

            # send the form submitted that is not valid back to register.html to display the errors, so users can fix it
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
                                                                                                                                                                                                                                                          
    # responsible for showing the form
    else:
        ''' user is not submitting the form, show them a blank registration form '''
        form = RegistrationForm()
        context = {'form': form}

        ##################  
        # printing the session id to a string
        request.session._session_key
        print "this is the sessionid: %s" % request.session._session_key
        ##################  

        return render_to_response('register.html', context, context_instance=RequestContext(request))
        
# don't name a method "Login" since Django already provides a method for that.       
def LoginRequest(request):

    if request.user.is_authenticated():        
        session_var = Session.objects.get(pk=request.session._session_key)
        print "this is the sessionid: %s" % session_var.get_decoded()
        return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))

    if request.method =='POST':

        ########################################################################
        request.session._session_key
        print "this is the sessionid: %s" % request.session._session_key
        ########################################################################

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            drinker = authenticate(username=username, password=password)
            # None: is the NULL variable in Python
        

            if drinker is not None:
                login(request, drinker)
                
                return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))

            else:
                # if there is an error, show the user the error
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    
    else:
        ''' user is not submitting the form, show the login form '''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))
    
    
def LogOutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')



# def indexer(request):
#     # rendering the response, also make the thankyou.html document
#     return render_to_response("index-image.html",
#                               locals(),
#                               context_instance=RequestContext(request))



# def get_images(request):
#     return


# TA's suggestion
# get_images function for the user 
# def get_images
# end
