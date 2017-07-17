# -*- coding: utf-8 -*-

from django.shortcuts import render
from site1.models import hosttable,usertable
import datetime

def Comparative_time():
    starttime = datetime.datetime.now()
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    result = hosttable.objects.values( 'dateTime')
    endtime = result[0]['dateTime'].strftime('%Y-%m-%d %H:%M:%S')
    d1 = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
    sum = (starttime-d1).seconds
    #if int(sum) > 600:
       # userinfo = usertable.objects.filter(hostname='llsserver_01').update(status ='0')
    #else:
        #userinfo = usertable(status='1')
    #userinfo.save()
    return sum