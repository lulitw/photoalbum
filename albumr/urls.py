from django.conf.urls import *
from albumr import views

# albumr related urls

urlpatterns = patterns('',
    url(r'^$', views.albums),
    url(r'(\d+)/edit/$', views.album_edit)

)
