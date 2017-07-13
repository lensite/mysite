# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from site1.models import usertable,hosttable
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.views.decorators import csrf

def home(request):
    result = hosttable.objects.values('hostname','hostip','hosthdd','hostmem','hostcpu')
    item_list = {}
    item_list['tr_list'] = result
    return render(request, "index.html",item_list)