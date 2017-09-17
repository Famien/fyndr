# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    context = {
        
            }
    return render(request, 'index.html', context)
def map(request):
    context = {

            }
    return render(request, 'map.html', context)
