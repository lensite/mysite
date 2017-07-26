# -*- coding: utf-8 -*-
from django.shortcuts import render
from site1.models import hoststate
def host_state(request):
    host_info= hoststate.objects.filter(hostid='2017072401').values('dateTime','interrecv').order_by('dateTime')
    state_list = {}
    state_list['inter'] = host_info
    return render(request, "charts.html",state_list)