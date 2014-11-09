from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

# How to log a user in (this will be in views.py)


# Create your views here.
# what our website is going to look like (what should be seen)

from .forms import SignUpForm

# this is the homepage of the web application
def home(request):
    
    form = SignUpForm(request.POST or None)
    
    # this notifies the user that the input boxed for the sign ups is filled or not
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Signing Up!')
        return HttpResponseRedirect('/thank-you/')
    
    # rendering the response
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))


def thankyou(request):
    
    # rendering the response, also make the thankyou.html document
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))



def aboutus(request):
    
    # rendering the response, also make the aboutus.html document and aboutus URL
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))