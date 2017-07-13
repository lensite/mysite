# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from site1.models import usertable,hosttable
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.views.decorators import csrf

def home(request):
    item_list1 = {}
    test = hosttable.objects.values('hostname','hostip','hosthdd','hostmem','hostcpu')
    for x in  test:
        print(x)
    result = hosttable.objects.filter(hostname='llsserver_01').values()[0]
    item_list = {}
    item_list['td_list'] = (result['hostname'],result['hostip'],result['hosthdd'],result['hostmem'],result['hostcpu'])
    print(item_list['td_list'])
    item_list['tr_list'] =(1,2,3,4,5,6,7,8)
    return render(request, "index.html",item_list)