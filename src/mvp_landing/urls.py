from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# not sure about line 7
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dropzone-drag-drop/$', include('dragdrop.urls', namespace="dragdrop", app_name="dragdrop")),   
    url(r'^index/$', 'dragdrop.views.GetUserImages'),
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^register/$', 'drinker.views.DrinkerRegistration'),
    url(r'^login/$', 'drinker.views.LoginRequest'),
    url(r'^logout/$', 'drinker.views.LogOutRequest'),
    url(r'^index/filter/$', 'filter.views.changeBright'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # not sure if I need an actual url wrapper in this code. 
    # url(r'^admin/varnish/', include('varnishapp.urls')),
)


if settings.DEBUG:
    # urlpatterns add STATIC_URL and serves the STATIC_ROOT file
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)