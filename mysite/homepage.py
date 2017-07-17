# -*- coding: utf-8 -*-

from django.shortcuts import render
from . import Calculation
from site1.models import hosttable
import datetime

def home(request):
    starttime = datetime.datetime.now()
    #endtime = datetime.datetime.now()
    #print((endtime - starttime).seconds)

    result = hosttable.objects.values('hostname','hostip','hosthdd','hostmem','hostcpu','dateTime')
    item_list = {}
    item_list['tr_list'] = result
    endtime = result[0]['dateTime'].strftime('%Y-%m-%d %H:%M:%S')
    d1 = datetime.datetime.strptime(endtime,'%Y-%m-%d %H:%M:%S')
    print((starttime-d1).seconds)
    print(Calculation.Comparative_time())
    return render(request, "index.html",item_list)