from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User

from albumr.utils import random_string
from django.utils import timezone

# Album Model
class Album(models.Model):
    name = models.CharField(max_length=200)
    unique_url = models.CharField(max_length=255, default=random_string(12))
    description = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(User, related_name='user_albums')

    def __unicode__(self):
        return self.name


class Page(models.Model):
    # default template layouts
    TEMPLATES = (
        (u'template1', u'template1'),
        (u'template2', u'template2'),
        (u'template3', u'template3'),
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
    # page item types (not currently used, only image is used)
    ITEM_TYPES = (
        (u'image', u'Image'),
        (u'text', u'Text'),
        )
    page = models.ForeignKey(Page, related_name='page_items')
    type = models.CharField(max_length=10, choices=ITEM_TYPES)
    position = models.IntegerField()
    value = models.TextField()

    # position should be 0, 1 or 2

    def save(self, *args, **kwargs):

        positions = self.page.page_items.values('position').order_by('position')
        allowed = [0,1,2]
        if self.id is not None :
          super(PageItem, self).save(**kwargs)

        # each page should not have more than 3 items
        if self.page.page_items.all().count() <  3:
            for p in positions:
                if p['position'] == self.position:
                   allowed.remove(self.position)
                   self.position = allowed[0]

            super(PageItem, self).save(**kwargs)

    class Meta:
        ordering = ['position']

