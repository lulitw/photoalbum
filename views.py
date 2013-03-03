from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import *
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages


from forms import MAuthForm, MUserCreationForm
from django.contrib.auth.models import User


def index(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('am_home'))

    form = MAuthForm()
    rform = MUserCreationForm(initial={'username':'default'})

    params = {'form': form, 'rform': rform }
    return render_to_response('welcome/index.html', params,  context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                HttpResponseRedirect(reverse('am_home'))
            else:
                messages.error(request, 'Account has been disabled')
        else:
            messages.error(request, 'Username/Password Invalid')

        return HttpResponseRedirect(reverse('home'))


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['username'] = 'default'
        form = MUserCreationForm(post)

        if form.is_valid():
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            pos = email.find('@')
            username = email[0:pos]

            if(password1 == password2):
                try:
                    user = User.objects.create_user(username, email, password1)

                    user = authenticate(username=username, password=password1)
                    auth_login(request, user)
                    HttpResponseRedirect(reverse('am_home'))
                except:
                    messages.error(request, 'User already exists')
                    return HttpResponseRedirect(reverse('am_home'))

            else:
                messages.error(request, 'Unable to create user')
        else:
            messages.error(request, 'Unable to create user', form.errors)

    return HttpResponseRedirect(reverse('am_home'))


