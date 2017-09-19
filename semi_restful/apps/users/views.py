# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from models import *
# Create your views here.
def users(request):
	context = { 'users': User.objects.all()}
	return render(request,"users/users.html",context)
def new(request):
	return render(request,"users/add.html")
def edit(request,id):
	context = {'user':User.objects.get(id=id)}
	return render(request,"users/edit.html",context)
def delete(request,id):
	u = User.objects.get(id=id)
	if u:
		u.delete()
	return redirect("/users")
def create(request):
	errors = User.objects.create_validator(request.POST)
	if len(errors):
		for tag,error in errors.iteritems():
			messages.error(request,error,extra_tags = tag)
		return redirect("/users/new")
	else:
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
		return redirect("/users")
def update(request,id):
	errors = User.objects.create_validator(request.POST)
	if len(errors):
		for tag,error in errors.iteritems():
			messages.error(request,error,extra_tags = tag)
		return redirect("/users/"+id+"/eidt")
	else:
		u = Users.objects.get(id=id)
		u.first_name=request.POST['first_name']
		u.last_name=request.POST['last_name']
		u.email=request.POST['email']
		u.save()
		return redirect("/users")
def show(request,id):
	print id
	context = {'user': User.objects.get(id=id)}
	return render(request,"users/show.html",context)