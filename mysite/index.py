# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from site1.models import usertable
from django.http import HttpResponseRedirect
from django.views.decorators import csrf

def sign_up(request):
    ctx = {}
    if  request.POST:
        RequestData = request.POST
        userinfo = usertable(uname=request.POST['usernamesignup'],
                 email=request.POST['emailsignup'],
                 password=request.POST['passwordsignup'])
        userinfo.save()
        ctx['zlt'] = '成功注册'
        return HttpResponseRedirect("/")
    return render(request, "sign_up.html",ctx)

def log_in(request):
    ctx = {}
    if request.POST:
        RequestData = request.POST
        RequestName = RequestData.get('username')
        RequestPasswd = RequestData.get('password')
        result = usertable.objects.filter(uname=RequestName,password=RequestPasswd).count()
        if result == 1:
            ctx['rlt'] = '登陆成功'
            return HttpResponseRedirect("/index")
        else:
            ctx['rlt'] = '登陆错误'
    return render(request, "log_in.html", ctx)