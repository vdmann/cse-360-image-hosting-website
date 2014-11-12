from django.conf.urls import patterns, include, url
from django.conf import settings
# Serving files uploaded by a user during development
from django.conf.urls.static import static

urlpatterns = patterns('',
	
	# The pattern includes a caret (^) and a dollar sign ($). These are regular 
	# expression characters that have a special meaning: the caret means require 
	# that the pattern matches the start of the string, and the dollar sign means 
	# require that the pattern matches the end of the string.
	# 
	# This concept is best explained by example. If we had instead used the 
	# pattern '^hello/' (without a dollar sign at the end), then any URL 
	# starting with /hello/ would match, such as /hello/foo and /hello/bar, 
	# not just /hello/. Similarly, if we had left off the initial caret 
	# character (i.e., 'hello/$'), Django would match any URL that ends with 
	# hello/, such as /foo/bar/hello/. If we had simply used hello/, without a 
	# caret or dollar sign, then any URL containing hello/ would match, such as 
	# /foo/hello/bar. Thus, we use both the caret and dollar sign to ensure that 
	# only the URL /hello/ matches nothing more, nothing less.
	# 
	# 
	# As explained in the last section youll see a 404 error message if you 
	# view the site root http://127.0.0.1:8000/. Django doesnt add magically 
	# anything to the site root that URL is not specialcased in any way. Its 
	# up to you to assign it to a URLpattern, just like every other entry in your 
	# URLconf.
	# 
	# The URLpattern to match the site root is a bit unintuitive, though, so 
	# its worth mentioning. When youre ready to implement a view for the site 
	# root, use the URLpattern '^$', which matches an empty string. For example:
	# 
	# so, are we representing '^$'' as the root? for dropzone-drag-drop.html?
    url(r'^$', 'dragdrop.views.DraggingAndDropping', name='DraggingAndDropping'),

# this is to deploy static files from media url
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
