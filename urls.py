from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'albumr.views.index', name='home'),

    url(r'^albums/', include('albumr.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()

