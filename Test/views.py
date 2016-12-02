from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from django.contrib.auth import login, logout, authenticate
from .Forms import UserForm, RegistForm
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
            #User.username = username
            #User.password = password
            #User.save()
            #response = HttpResponseRedirect('/Test/login/')
            #return response
            #return HttpResponse('register successfully!')
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

            if user:
                response = HttpResponseRedirect('/Test/index/')
                response.set_cookie('username', username, 3600)
                return response
                #return render(req, '/Test/index/', context_instance=RequestContext)

            else:
                HttpResponseRedirect('/Test/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))

def index(req):
    username = req.COOKIES.get('username')
    return render_to_response('index2.html', {'username': username})

def logout(req):
    #response = HttpResponse("You have successfully loggout")
    response = HttpResponseRedirect('/Test/login/')
    response.delete_cookie('username')
    uf = UserForm()
    return render_to_response('login.html', {'uf': uf})


