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
    hosttable.objects.filter(dateTime__gte=Final_time,dateTime__lte=Current_time).update(status=1)
    hosttable.objects.filter(dateTime__lt=Final_time).update(status=0)