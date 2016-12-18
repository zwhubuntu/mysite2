#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from django.contrib.auth import login, logout, authenticate
from .Forms import UserForm, RegistForm, SearchForm
<<<<<<< Updated upstream
from models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
=======
from models import User, MyUser
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import django_excel as excel
import csv
>>>>>>> Stashed changes


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
                    pwd = make_password(password, None, 'pbkdf2_sha256')
                    MyUser.objects.create(username=username, password=pwd)
                    return HttpResponse('Register Successfully!')
                else:
                    return HttpResponse('Please confirm your password!')
            except:
                pass
        else:
            rf = RegistForm()
    else:
        rf = RegistForm()
    return render_to_response('regist.html', {'rf': rf}, context_instance=RequestContext(req))


def mylogin(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #user = User.objects.filter(username__exact=username, password__exact=password)
            user = authenticate(username=username, password=password)
            #user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                login(req, user)
                req.session["username"] = username
                response = HttpResponseRedirect('/Test/index/')
                response.set_cookie('username', username, 3600)
                tmp_count = MyUser.objects.get(username__exact=username)
                tmp_count.log_count += 1
                tmp_count.last_log_ip = req.META['REMOTE_ADDR']
                tmp_count.save()
                return response
<<<<<<< Updated upstream
                #return render(req, '/Test/index/', context_instance=RequestContext)
=======
            else:
                uf = UserForm()
                return render_to_response('login.html', {'uf': uf, 'flag': True}, context_instance=RequestContext(req))
>>>>>>> Stashed changes
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))

<<<<<<< Updated upstream
#@login_required
=======
#@login_required()#(login_url= "/Test/login")
>>>>>>> Stashed changes
def index(req):
    #flag = req.session["user_id"]
    username = req.COOKIES.get('username')
<<<<<<< Updated upstream
    if req.method == "POST":
        sf = SearchForm(req.POST)
        if sf.is_valid():
            username = sf.cleaned_data['username']
            users = User.objects.filter(username__exact=username)
            if users:
                #users = User.objects.get(username__exact=username)
                #print users.username
                return render_to_response('index2.html', {'username': username, 'users': users, 'sf': sf}, context_instance=RequestContext(req))
    else:
        sf = SearchForm()
        return render_to_response('index2.html', {'username': username, 'sf': sf}, context_instance=RequestContext(req))
    sf = SearchForm()
    users = User.objects.all()
    return render_to_response('index2.html', {'username': username, 'users': users, 'sf': sf})

=======
    login_flag = req.user.is_authenticated()
    print login_flag
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/Test/login/',{'login_flag':True})
    else:
        return render_to_response('index2.html', {'username': username}, context_instance=RequestContext(req))
>>>>>>> Stashed changes


@login_required()
def mylogout(req):
    #response = HttpResponse("You have successfully loggout")
    response = HttpResponseRedirect('/Test/login/')
    response.delete_cookie('username')
    logout(req)
    del req.session
    #req.session.delete()
    #req.session.save()
    #del req.session
    uf = UserForm()
    return render_to_response('login.html', {'uf': uf})

<<<<<<< Updated upstream
=======
@login_required()
def home(req):
    if req.method=="POST":
        sf = SearchForm(req.POST)
        if sf.is_valid():
            username = sf.cleaned_data['username']
            users = MyUser.objects.filter(username__contains=username)
            if users:
                return render_to_response('home.html', {'users': users, 'sf': sf},context_instance=RequestContext(req))
            else:
                return render_to_response('home.html', {'sf': sf}, context_instance=RequestContext(req))
        else:
            return render_to_response('home.html', {'sf': sf}, context_instance=RequestContext(req))
    sf = SearchForm()
    users = MyUser.objects.all()
    return render_to_response('home.html', {'sf': sf},context_instance=RequestContext(req))

@login_required()
def export_excel(req):
    users = MyUser.objects.all()
    response = HttpResponse(users, content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment;filename="download.xls"'
    writer = csv.writer(response)
    for user in users:
        writer.writerow([user.id, user.username, user.last_login, user.log_count, user.last_log_ip])
    return response

>>>>>>> Stashed changes


