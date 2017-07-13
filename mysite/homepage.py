# -*- coding: utf-8 -*-

from django.shortcuts import render
from site1.models import hosttable
import datetime

def home(request):
    starttime = datetime.datetime.now()
    endtime = datetime.datetime.now()
    print(starttime)
    print((endtime - starttime).seconds)

    result = hosttable.objects.values('hostname','hostip','hosthdd','hostmem','hostcpu')
    item_list = {}
    item_list['tr_list'] = result
    return render(request, "index.html",item_list)