from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from login.models import Users
from django.template import RequestContext
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def ListCS(request):
    return render(request, 'ListCS.html')


class userForm(forms.Form):
    inputTel = forms.CharField(label='inputTel', max_length=12)
    inputPassword = forms.CharField(label='inputPassword', widget=forms.PasswordInput())


def log(req):
    if req.method == 'POST':
        uf = userForm(req.POST)
        if uf.is_valid():
            inputTel = uf.cleaned_data['inputTel']
            inputPassword = uf.cleaned_data['inputPassword']
            user = Users.objects.filter(userTel=inputTel, userPwd=inputPassword)
            if user:
                response = HttpResponseRedirect('/login/log/')
                response.set_cookie('inputTel', inputTel, 3600)
                req.session['inputTel'] = "inputTel"
                return render(req, 'index.html')
            else:
                return HttpResponseRedirect('login/navbar/')
    else:
        uf = Form()
    return HttpResponseRedirect('/login/')
