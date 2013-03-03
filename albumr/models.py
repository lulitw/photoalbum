from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User

from albumr.utils import random_string

class Album(models.Model):
    name = models.CharField(max_length=200)
    unique_url = models.CharField(max_length=255, default=random_string(12))
    description = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(User, related_name='user_albums')

    def __unicode__(self):
        return self.name


class Page(models.Model):
    TEMPLATES = (
        (u'template1', u'template1'),
        (u'template2', u'template2'),
        (u'template3', u'template3'),
        (u'template4', u'template4'),
        )
    album = models.ForeignKey(Album, related_name='pages')
    caption = models.CharField(max_length=200)
    template =  models.CharField(max_length=100)
    position = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.caption

    class Meta:
        ordering = ['position']


class PageItem(models.Model):
    ITEM_TYPES = (
        (u'image', u'Image'),
        (u'text', u'Text'),
        )
    page = models.ForeignKey(Page, related_name='page_items')
    type = models.CharField(max_length=10, choices=ITEM_TYPES)
    position = models.IntegerField()
    value = models.TextField()

    class Meta:
        ordering = ['position']

