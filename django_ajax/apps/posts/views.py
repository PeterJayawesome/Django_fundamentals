# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.
def posts(request):
	posts = Post.objects.all()
	return render(request,"posts/posts.html",{'posts': posts})

def add_note(request):
	if request.method == "POST":
		print "submit"
		Post.objects.create(content=request.POST['content'])
		post = Post.objects.last()
		return render(request,"posts/new_post.html",{"new_post": post})