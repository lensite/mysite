# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from site1.models import usertable
from django.http import HttpResponseRedirect
from django.views.decorators import csrf

def home(request):
    ctx = {}

    return render(request, "index.html",ctx)