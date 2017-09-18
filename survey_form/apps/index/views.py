# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
def survey_form(request):
	request.session.clear()
	return render(request,'index/survey.html')
def result(request):
	return render(request, 'index/result.html')
def process(request):
	if request.method == 'POST':
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return redirect('/result')
	return redirect('/')