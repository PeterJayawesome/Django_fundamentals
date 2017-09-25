# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import models
# Create your views here.
def main(request):
	request.session['log'] = False
	return render(request,"wishlist/log.html")
def dashboard(request):
	if 'log' in request.session:
		wish_list = User.objects.wish_list.all()
		id_list = [item.id for item in wish_list]
		other_items = Item.objects.exclude(id__in=id_list)
		context = {
			"list": wish_list,
			"other_items": other_items,
		}
	return render(request,"wishlist/dashboard.html",context)
def item(request,id):
	items = Item.objects.filter(id=id)
	if items:
		user_list = items[0].wished_by.all()
		context = {
			"item": items[0]
			"user_list": user_list
		}
		return render(request,"wishlist/item.html",context)
	return
def add_item(request):
	return
def login(request):
	if request.method == "POST":
		request.session['log_reg'] = 'log'
		error = User.objects.login_check(request.POST)
		if len(error):
			messages.error(request,"Email and password not match",extra_tags="login")
			return redirect('/main')
		else:
			request.session['log'] = True
			request.session['user_id'] = User.objects.get(username = request.POST['username']).id
			return redirect('/dashboard')
	return redirect('/main')
def reg(request):
	if request.method == "POST":
		request.session['log_reg']='reg'
		errors = User.objects.reg_validator(request.POST)
		if len(errors):
			for tag,error in errors.iteritems():
				messages.error(request,error,extra_tags=tag)
			return redirect('/main')
		secure_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
		User.objects.create(name=request.POST['name'],username = request.POST['username'],date_hired = request.POST['date'],password = secure_password)
		request.session['log'] = True
		request.session['user_id'] = User.objects.get(username=request.POST['username'])
		return redirect('/dashboard')
	return redirect('/main')
def remove(request):
	return
def delete(request):
	return
def add(request):
	return
def create(request):
	return