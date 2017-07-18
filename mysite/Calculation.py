# -*- coding: utf-8 -*-

from django.shortcuts import render
from site1.models import hosttable,usertable
import datetime
import time

def Comparative_time():
    starttime = datetime.datetime.now()
    Five_Minutes = datetime.timedelta(seconds=120)
    Final_time = (starttime - Five_Minutes).strftime('%Y-%m-%d %H:%M:%S')
    Current_time = (starttime + Five_Minutes).strftime('%Y-%m-%d %H:%M:%S')
    print(Final_time)
    print(Current_time)
    hosttable.objects.filter(dateTime__gte=Final_time,dateTime__lte=Current_time).update(status=1)
    hosttable.objects.filter(dateTime__lt=Final_time).update(status=0)
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    #result = hosttable.objects.values( 'hostname','dateTime')
    #endtime = datetime.datetime.strptime(result[0]['dateTime'].strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    #hosttable.objects.filter(status=).update(status=0)
    #if (starttime-d1).seconds > 600:
        #hosttable.objects.filter(hostname='11').update(status = 0)
    #else:
        #hosttable.objects.filter(hostname='11').update(status = 1)


