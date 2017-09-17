# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request, name):
    context = {
            'name': name
            }
    return render(request, 'web_fyndr/index.html', context)
