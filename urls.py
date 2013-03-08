from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


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
urlpatterns += staticfiles_urlpatterns()

