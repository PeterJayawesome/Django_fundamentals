# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import strftime,localtime
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
	context = {
	"time": strftime("%Y-%m-%d %H:%M %p", localtime())
	}
	print context
	return render(request,'displaytime/index.html',context)