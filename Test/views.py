from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from django.contrib.auth import login, logout, authenticate
from .Forms import UserForm, RegistForm, SearchForm
from models import User


# Create your views here.
def regist(req):
    #return render_to_response('regist.html')
    if req.method == 'POST':
        #uf = UserForm(req.POST)
        rf = RegistForm(req.POST)
        if rf.is_valid():
            username = rf.cleaned_data['username']
            password = rf.cleaned_data['password']
            confirm_password = rf.cleaned_data['confirm_password']
            try:
                if password == confirm_password:
                    User.objects.create(username=username, password=password)
                    return HttpResponse('Register Successfully!')
                else:
                    return HttpResponse('Please confirm your password!')
            except:
                pass
        else:
            rf = RegistForm()
    else:
        rf = RegistForm
    return render_to_response('regist.html', {'rf': rf}, context_instance=RequestContext(req))


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact=password)
            #tmp_count = User.objects.filter(username__exact=username, password__exact=password).values('log_count')
            #print tmp_count
            if user:
                response = HttpResponseRedirect('/Test/index/')
                response.set_cookie('username', username, 3600)
                tmp_count = User.objects.get(username__exact=username, password__exact=password)
                tmp_count.log_count += 1
                tmp_count.save()
                return response
                #return render(req, '/Test/index/', context_instance=RequestContext)

            else:
                HttpResponseRedirect('/Test/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))

def index(req):
    username = req.COOKIES.get('username')
    '''
    if req.method == "POST":
        sf = SearchForm(req.POST)
        if sf.is_valid():
            username = sf.cleaned_data['username']
            user_get = User.objects.filter(username__exact=username)
            if user_get:
                users = User.objects.get(username__exact=username)
                print users.username
                return render_to_response('index2.html', {'username': username, 'users': users, 'sf': sf},context_instance=RequestContext(req))
            elif username== '':
                users = User.objects.all()
                return render_to_response('index2.html', {'username': username, 'users': users, 'sf': sf},context_instance=RequestContext(req))
            else:
                users = User.objects.all()
                return render_to_response('index2.html', {'username': username, 'users': users, 'sf': sf},context_instance=RequestContext(req))
    else:
        sf = SearchForm()
        return render_to_response('index2.html', {'username': username, 'sf': sf},context_instance=RequestContext(req))
        '''
    sf = SearchForm()
    users = User.objects.all()
    return render_to_response('index2.html', {'username': username, 'users': users, 'sf': sf})



def logout(req):
    #response = HttpResponse("You have successfully loggout")
    response = HttpResponseRedirect('/Test/login/')
    response.delete_cookie('username')
    uf = UserForm()
    return render_to_response('login.html', {'uf': uf})

def showusers(req):
    users = User.objects.all()
    for user in users:
        print user.username
    return render_to_response('index2.html', {'users': users})



