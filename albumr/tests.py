from django.test import TestCase
from albumr.models import Album, Page, PageItem
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
import time
from django.test.client import Client
from django.core.urlresolvers import reverse
import random
from factories import PageItemFactory, UserFactory, AlbumFactory, PageFactory

from django.db.models import Q


# Test that all pages are loaded properly
# Also test for authenticated/non-authenticated views

class NonLoggedPagesTest(TestCase):
    fixtures = ['test_data',]

    def setup(self):
        self.client = Client()

    # non - logged in users should be able to see the landing page
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200, "Testing that a status code 200 is returned by the view")

        response = self.client.get(reverse('am_home'), follow=True)
        self.assertRedirects(response, '/?next=/albums/')
        self.assertTemplateUsed(response, "welcome/index.html", "Test welcome/index.html template is used")

    def test_album_public(self):
        user = User.objects.get(username='joe')
        ualbum = user.user_albums.all()[0];

        # get the album public url

        response = self.client.get(reverse('am_public', args=(ualbum.unique_url,)))
        self.assertTemplateUsed( response, 'album/album_public.html' )

        self.assertEqual(response.status_code, 200);



class LoggedPagesTest(TestCase):

    fixtures = ['test_data',]


    def setup(self):
        self.client = Client()

    # test logged in users view
    def test_home(self):

        user = User.objects.create_user('testo', 'tester@tester.com', 'testo')
        self.client.login(username='testo', password='testo')

        response = self.client.get('/', follow=True)

        # Test that landing page redirects to albums page for logged in users
        self.assertRedirects(response, reverse('am_home'))
        self.assertTemplateUsed(response, "album/album.html", "Test album template is used")

    def test_album_list(self):

        self.client.login(username='joe', password='joe')

        user = User.objects.get(username='joe')
        response = self.client.get(reverse('am_home'), follow=True)
        self.assertContains(response, user.user_albums.all()[0], 1, 200, 'Test that the list contains at least the first item')

        User.objects.create_user('hans', '', 'hans')
        self.client.login(username='hans', password='hans')

        response = self.client.get(reverse('am_home'), follow=True)
        self.assertContains(response, 'No albums found', 1, 200, 'Test that a user with no albums get the right text')


    def test_album_edit(self):
        self.client.login(username='joe', password='joe')
        user = User.objects.get(username='joe')

        #get the first album of user
        ualbum = user.user_albums.all()[0]
        response = self.client.get(reverse('am_edit', args=(ualbum.id,)), follow=True)

        # album view
        self.assertContains(response, ualbum.name, 1, 200, 'Detailed album view')

        #not found
        response = self.client.get(reverse('am_edit', args=(random.randint(100,1000),)), follow=True)
        self.assertEquals(response.status_code, 404)

        #access restriction
        other_albums = Album.objects.exclude(owner = user)
        response = self.client.get(reverse('am_edit', args=(other_albums[0].id,)), follow=True)

        messages = list(response.context['messages'])

        # Test that user does not have access to other user's albums
        self.assertRedirects(response, reverse('am_home'))
        self.assertEqual(str(messages[0]), 'You are not allowed to access that.')



    def test_album_delete(self):

        self.client.login(username='joe', password='joe')
        user = User.objects.get(username='joe')

        #get the first album of user
        ualbum = user.user_albums.all()
        ucount = ualbum.count()
        aid = ualbum[0].id

        response = self.client.get(reverse('am_delete', args=(aid,)), follow=True)

        self.assertRedirects(response, reverse('am_home'))
        self.assertEqual(user.user_albums.all().count(), ucount - 1, "Test that album count has decreased")

        response = self.client.get(reverse('am_delete', args=(aid,)), follow=True)
        self.assertEqual(response.status_code, 404)

        #access restriction
        other_albums = Album.objects.exclude(owner = user)
        response = self.client.get(reverse('am_edit', args=(other_albums[0].id,)), follow=True)

        messages = list(response.context['messages'])

        # Test that user does not have access to other user's albums
        self.assertRedirects(response, reverse('am_home'))
        self.assertEqual(str(messages[0]), 'You are not allowed to access that.')




class AlbumModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')

    def test_creating_and_saving_album(self):

        album = Album()
        album.name= "New Album"
        album.description = "Very good album."
        album.owner = self.user

        album.save()

        # check if album has been saved
        all_albums = Album.objects.all()
        self.assertEquals(len(all_albums), 1, "Testing that length of albums created")
        album_in_database = all_albums[0]
        self.assertEquals(album_in_database, album, "Testing that the new created album is only one in database")

        # check the value of attributes
        self.assertEquals(album_in_database.name, "New Album")
        self.assertEquals(album_in_database.description, album.description)

        #print album_in_database.created
        #self.assertEquals(album_in_database.created, timezone.now(), 'Check created timestamp is set properly')

        # check user's own albums
        user_albums = self.user.user_albums.all()
        self.assertEquals(user_albums.count(), 1, "Check the amount of user albums")



class PageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')

    def test_create_page_for_album(self):
        # create album object
        album = Album()
        album.name= "New Album"
        album.description = "Very good album."
        album.owner = self.user

        album.save()

        # create page
        page = Page()

        # link it with album
        page.album = album

        page.caption = "Caption for All"
        page.position = 0
        page.template = 'template1';

        page.save()

        # try retrieving it from the database
        album_pages = album.pages.all()
        self.assertEquals(album_pages.count(), 1, 'Check that amount of pages album has')
        self.assertEquals(album_pages[0], page, 'Check the page created is equal to the albums page')


        # check attributes have been saved
        page_from_db =  Page.objects.all()[0]
        self.assertEquals(page_from_db, page,)
        self.assertEquals( page_from_db.caption, page.caption)
        self.assertEquals( page_from_db.position, page.position)


class PageItemModelTest(TestCase):

    def setup(self):
        self.user = UserFactory()

    def test_position_unique(self):
        user = UserFactory()
        album = AlbumFactory.create(owner=user)
        page = PageFactory.create(album=album)

        item1 = PageItemFactory.create(page=page, value='item1') #initialized with position 0
        item2 = PageItemFactory.create(page=page, value='item2') #initialized with position 0
        item3 = PageItemFactory.create(page=page, position=0, value='item3') #initialized with position 0
        item4 = PageItemFactory.create(page=page, value='item4') #initialized with position 0

        self.assertNotEqual(item1.position, item2.position, "Test that no two items have the same position")

    def test_max_three_items_per_page(self):

        user = UserFactory()
        album = AlbumFactory.create(owner=user)
        page = PageFactory.create(album=album)

        PageItemFactory.create(page=page)
        PageItemFactory.create(page=page)
        PageItemFactory.create(page=page)
        PageItemFactory.create(page=page)

        self.assertEquals(3, page.page_items.all().count(), 'Test that a page has at maximum three items')



