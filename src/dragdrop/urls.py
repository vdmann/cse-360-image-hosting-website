from django.conf.urls import patterns, include, url
from django.conf import settings
# Serving files uploaded by a user during development
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'dragdrop.views.DraggingAndDropping', name='DraggingAndDropping'),
)
# this is to deploy static files from media url
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
