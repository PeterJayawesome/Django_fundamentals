# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render,redirect

# Create your views here.
def random_word(request):
	if 'attempt' not in request.session:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] +=1
	context = {
	'random_word': get_random_string(length = 14)
	}
	return render(request,'random_word/index.html',context)
def reset(request):
	request.session.clear()
	return redirect('http://localhost:8000/random_word')