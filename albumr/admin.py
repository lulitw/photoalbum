from django.contrib import admin

from albumr.models import Album, Page, PageItem

admin.site.register(Album)
admin.site.register(Page)
admin.site.register(PageItem)