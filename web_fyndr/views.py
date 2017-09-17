# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from classifier import *
import psycopg2

try:
	conn = psycopg2.connect("dbname='d9eu2mf4n8hcq4' user='oevfewnurxkiyq' host='ec2-23-21-186-138.compute-1.amazonaws.com' password='59e1ccde40a94e32af13a27b3866969c92b83a41474c4b3cde782348cf8985ca'")
except:
	print("can't connect to database")

def get_pic(request):
	pic_name = "3-7dwf.png"
	print("pic name " + pic_name)
	return HttpResponse("/media/" + pic_name, content_type="image/png")

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

		url = "radiant-forest-23095.herokuapp.com/media/" + filename
		print('url: ' + url)
		getTags(url)
		print("filename: " + filename)
		uploaded_file_url = fs.url(filename)
		return render(request, 'index.html', context)

	return render(request, 'index.html', context)

def map(request):
	print("map")
	context = {}
	return render(request, 'map_location_current.html', context)

def simple_upload(request):
	print("simple ")

def find_rooms(request):
	print("calling from here")
	cur = conn.cursor()
	cur.execute("""SELECT * FROM fyndr_rooms""")
	rows = cur.fetchall()
	return JsonResponse({"data": rows})


