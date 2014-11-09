# 2. These custom urls will override the main Photologue urls, so place them 
# just before Photologue in the project’s main urls.py file:
from django.conf.urls import *

# We’ve copied the urlpattern for the gallery list view from Photologue itself, 
# and changed it slightly by passing in paginate_by=5.
# And that’s it - now when that page is requested, our customised urls.py will 
# be called first, with pagination set to 5 items.
from photologue.views import GalleryListView

urlpatterns = patterns('',

                       # url(r'^gallerylist/$',
                       #     GalleryListView.as_view(paginate_by=5), name='photologue_custom-gallery-list'),
	             

					   # Changing views.py to create a for RESTful api
	                   url(r'^photolist/$',
	                       PhotoJSONListView.as_view(),
	                       name='photologue_custom-photo-json-list'),

                       )