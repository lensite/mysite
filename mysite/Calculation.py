# -*- coding: utf-8 -*-

from django.shortcuts import render
from site1.models import hosttable
import datetime

def Comparative_time():
    starttime = datetime.datetime.now()
    result = hosttable.objects.values('dateTime')
    endtime = result[0]['dateTime'].strftime('%Y-%m-%d %H:%M:%S')
    d1 = datetime.datetime.strptime(endtime,'%Y-%m-%d %H:%M:%S')
    return ((starttime-d1).seconds)