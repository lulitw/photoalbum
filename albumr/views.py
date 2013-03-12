# Create your views here.
from django.http import HttpResponse
from django.template import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.core.urlresolvers import reverse
from django.contrib import auth
from django.utils import simplejson

from django.contrib.auth.decorators import login_required

from albumr.models import Album, Page, PageItem
from albumr.forms import AlbumForm

#home page view for authenticated users
@login_required
def albums(request):
    form = AlbumForm(
        initial={'owner': request.user}
    )
    params = {'form': form }
    return render_to_response('album/album.html', params,  context_instance=RequestContext(request))

@login_required
def album_save(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.save()
            messages.success(request, "Album was created.")
        else:
            messages.error(request, 'Unable to create Album.', form.errors)
            #print 'form is not valid ! ', form.errors


    return HttpResponseRedirect('/albums/')


@login_required
def album_edit(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.user.id != album.owner.id:
        messages.error(request, "You are not allowed to access that.")
        return HttpResponseRedirect(reverse('am_home'))

    params = {'album': album}
    return render_to_response('album/album_edit.html', params,  context_instance=RequestContext(request))

def album_delete(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.user.id != album.owner.id:
        messages.error(request, "You are not allowed to access that.")
        return HttpResponseRedirect(reverse('am_home'))

    album.delete()
    messages.success(request, "Album was deleted.")
    return HttpResponseRedirect(reverse('am_home'))

# public view of albums
def album_public(request, album_unique_url):

    album = get_object_or_404(Album, unique_url=album_unique_url)
    params = {'album': album}

    return render_to_response('album/album_public.html', params,  context_instance=RequestContext(request))

#print album information in JSON format for the album editor

@login_required
def album_get(request, album_id):

    album = get_object_or_404(Album, id=album_id)
    result = {}
    result['name'] = album.name
    result['pages'] = album_json(album) # JSONify page elements

    return HttpResponse(simplejson.dumps(result), mimetype='application/json')


def album_json(album):
    result = []
    for page in album.pages.all():
        items = []
        #for item in page.page_items.all():
        for j, item in enumerate(page.page_items.all()):
            i = {
                'id': item.id,
                'position': item.position,
                'image_url': item.value
            }
            items.append(i)

        p = {
            'id': page.id,
            'name': page.caption,
            'position': page.position,
            'template': page.template,
            'items': items
        }
        result.append(p)
    return result

@login_required
def album_save_all(request):
    result = request.POST['json']
    result = simplejson.loads(result)

    album = get_object_or_404(Album, id=result['album_id'])

    c = 0 # this counter is used to correctly set the page position if a page has been deleted

    for i, p in enumerate(result['pages']):
        # handle existing pages
        if type(p['page_id']) is int:
            page = Page.objects.get(pk=p['page_id'])
            # if a page is deleted, the _destroy property will be set
            if(p.has_key('_destroy') and p['_destroy']):
                page.delete()
                c -= 1
                break
        # create new page, since it doesnt exist
        else:
            page = Page()
            page.album = album

        page.caption = p['page_name']
        page.template = p['template']
        page.position =  c
        page.save()

        items = []
        for j, it in enumerate(p['items']):
            if j > 2: # no more than 3 items -> obsolete, now save method handles this
                break
            if(it.has_key('item_id') and it['item_id']):
                item = PageItem.objects.get(pk=it['item_id'])
            else:
                item = PageItem()
                item.page = page

            item.value = it['image_url'] if it.has_key('image_url') else ''
            item.type = 'image' # other type is not used, default is image
            item.position = it['position']
            item.save()
            items.append(item.id)

        # clear up other items
        PageItem.objects.filter(page=page).exclude(id__in=items).delete()

        c += 1

    result = {}
    result['name'] = album.name
    result['pages'] = album_json(album)

    return HttpResponse(simplejson.dumps(result), mimetype='application/json')
