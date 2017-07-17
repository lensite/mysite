# -*- coding: utf-8 -*-

from django.shortcuts import render
from site1.models import hosttable,usertable
import datetime

def Comparative_time():
    starttime = datetime.datetime.now()
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    #result = hosttable.objects.values( 'hostname','dateTime')
    #endtime = datetime.datetime.strptime(result[0]['dateTime'].strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    #hosttable.objects.filter(status=).update(status=0)
    #if (starttime-d1).seconds > 600:
        #hosttable.objects.filter(hostname='11').update(status = 0)
    #else:
        #hosttable.objects.filter(hostname='11').update(status = 1)
    Five_Minutes = datetime.timedelta(seconds=300)
    Final_time = (starttime+Five_Minutes).strftime('%Y-%m-%d %H:%M:%S')
    hosttable.objects.filter(dateTime__gte=Final_time).update(status=1)
    hosttable.objects.filter(dateTime__lte=Final_time).update(status=0)