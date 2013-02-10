# Create your views here.
from django.http import HttpResponse
from django.template import *
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import auth

def index(request):
	return render_to_response('welcome/index.html', {},  context_instance=RequestContext(request))



def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")
