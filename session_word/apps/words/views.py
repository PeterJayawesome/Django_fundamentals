# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from time import strftime,localtime
# Create your views here.
def index(request):
	if 'words' not in request.session:
		request.session['words']= []
	print request.session['words']
	return render(request,'words/session_words.html')
def clear(request):
	request.session.clear()
	return redirect('/session_words')
def add_word(request):
	if request.method == 'POST':
		request.session['words'].append({
			'word': request.POST['word'],
			'color': request.POST['color'],
			'size': 'normal',
			'time': strftime("%I:%M:%S%p, %B %d%Y")
		})
		# request.session['test'] = 1 #without this line words can not be appended? WHY?
		print request.session['words']
		if 'size' in request.POST:
			request.session['words'][-1]['size'] = 'big'
	return redirect('/session_words')