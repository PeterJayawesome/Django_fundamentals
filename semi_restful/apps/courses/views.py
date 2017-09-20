# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from models import *

# Create your views here.
def index(request):
	courses = Course.objects.all()
	context = {
		"courses" : courses
	}
	return render(request,"courses/index.html", context)
def delete(request,id):
	course = Course.objects.get(id=id)
	context = {"course":course}
	return render(request,"courses/delete.html",context)
def comments(request,id):
	course = Course.objects.get(id=id)
	context = {"course": course,"comments": course.comments.all()[::-1]}
	return render(request,"courses/comments.html",context)
def add(request):
	if request.method == "POST":
		errors = False
		error = Course.objects.basic_validator(request.POST)
		if len(error):
			messages.error(request,error['name'],extra_tags='name')
			errors = True
		error = Description.objects.basic_validator(request.POST)
		if len(error):
			messages.error(request,error['desc'],extra_tags='desc')
			errors = True
		if errors:
			return redirect("/courses")
		else:
			Course.objects.create(name=request.POST['name'])
			Description.objects.create(content=request.POST['desc'],course=Course.objects.last())
			course = Course.objects.last()
			course.desc = Description.objects.last()
			course.save()
			return redirect("/courses")
def remove(request,id):
	if request.method == "POST":
		course = Course.objects.get(id=id)
		if course:
			course.delete()
	return redirect("/courses")
def create(request,id):
	if request.method == "POST":
		Comment.objects.create(content=request.POST['content'],course=Course.objects.get(id=id))
	return redirect('/courses/'+id+'/comments')