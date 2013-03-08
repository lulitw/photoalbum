import factory
from models import User, Album, Page, PageItem

class UserFactory(factory.Factory):
    FACTORY_FOR = User
    username= 'Jane'
    password = 'Jane'
    #admin = False

class AlbumFactory(factory.Factory):
    FACTORY_FOR = Album
    name = 'test album'
    owner = factory.SubFactory(UserFactory)

class PageFactory(factory.Factory):
    FACTORY_FOR = Page
    caption = 'first page'
    position = 0
    template = 'template1'
    album = factory.SubFactory(AlbumFactory)


class PageItemFactory(factory.Factory):
    FACTORY_FOR = PageItem
    type = 'image'
    position = 0
    page = factory.SubFactory(PageFactory)
    value = 'imgurl.com/'

