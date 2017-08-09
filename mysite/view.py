# -*- coding: utf-8 -*-
from django.shortcuts import render
from site1.models import usertable,hosttable,hoststate
from django.http import HttpResponseRedirect,HttpResponse
from . import Calculation,charts
import json

def sign_up(request):
    ctx = {}
    if  request.POST:
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

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def host_list(request):
    host_list = hosttable.objects.\
        values('hostname','hostid','hostip','hosthdd','hostmem','hostcpu','dateTime','status')
    host_info= hoststate.objects.filter(hostid='2017072401').\
        values('dateTime','interrecv','intersent','cpustate','memstate').order_by('dateTime')
    item_list = {}
    item_list['inter'] = host_info
    item_list['tr_list'] = host_list
    Calculation.Comparative_time()
    return render(request, "index.html",item_list)