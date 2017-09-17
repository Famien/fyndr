# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage


def index(request):
	print("index")
	context = {}

	if request.method == 'GET':
		print('get')
		return render(request, 'index.html', context)

	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print("filename: " + filename)
        uploaded_file_url = fs.url(filename)
        
        return render(request, 'index.html', context)


	return render(request, 'index.html', context)
def map(request):
	print("map")
	context = {}
	return render(request, 'map.html', context)

def simple_upload(request):
	print("simple ")
