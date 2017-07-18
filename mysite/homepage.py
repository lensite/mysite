# -*- coding: utf-8 -*-

from django.shortcuts import render
from . import Calculation
from site1.models import hosttable

def host_list(request):
    result = hosttable.objects.values('hostname','hostid','hostip','hosthdd','hostmem','hostcpu','dateTime','status')
    item_list = {}
    item_list['tr_list'] = result
    Calculation.Comparative_time()
    return render(request, "index.html",item_list)