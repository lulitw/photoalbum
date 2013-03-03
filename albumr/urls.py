from django.conf.urls import *
from albumr import views

# albumr related urls

urlpatterns = patterns('',
    url(r'^$', views.albums, name='am_home'),

    url(r'(\d+)/edit/$', views.album_edit, name='am_edit'),
    url(r'(\d+)/delete/$', views.album_delete, name='am_delete'),

    url(r'^save/$', views.album_save, name='am_save'),

    url(r'^get/(\d+)/$', views.album_get),
    url(r'^save_all/$', views.album_save_all, name='am_save_all')




)
