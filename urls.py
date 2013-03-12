from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
from albumr import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'views.index', name='home'),
    url(r'^social_auth/', include('social_auth.urls')),
    url('^login/$', 'views.login', name='login'),
    url('^logout/$', 'views.signout', name='logout'),
    url('^signup/$', 'views.signup', name='signup'),



    url(r'^albums/', include('albumr.urls')),
    url(r'^(\w+)/$', views.album_public, name='am_public'),


)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
else:
    urlpatterns += patterns('',
    (r'static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
