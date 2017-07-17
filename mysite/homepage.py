# -*- coding: utf-8 -*-

from django.shortcuts import render
from site1.models import hosttable
import datetime
import time

def home(request):
    starttime = datetime.datetime.now()
    #endtime = datetime.datetime.now()
    #print((endtime - starttime).seconds)
    result = hosttable.objects.values('hostname','hostip','hosthdd','hostmem','hostcpu','dateTime')
    item_list = {}
    item_list['tr_list'] = result
    return render(request, "index.html",item_list)