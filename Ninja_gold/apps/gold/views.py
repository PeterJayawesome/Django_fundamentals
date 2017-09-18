# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from random import randint
from time import strftime,localtime
# Create your views here.
def gold(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activity' not in request.session:
		request.session['activity'] = []
	return render(request,'gold/gold.html')
def farm(request):
	if request.method == 'POST':
		earned = randint(10,20)
		request.session['activity'].append({'color': 'green','text': "Earned {} golds from the {}! ({})".format(earned,'farm',strftime("%Y/%m/%d %I:%M %p"))})
		request.session['gold'] += earned
	return redirect('/')
def cave(request):
	if request.method == 'POST':
		earned = randint(5,10)
		request.session['activity'].append({'color': 'green','text': "Earned {} golds from the {}! ({})".format(earned,'cave',strftime("%Y/%m/%d %I:%M %p"))})
		request.session['gold'] += earned
	return redirect('/')
def house(request):
	if request.method == 'POST':
		earned = randint(2,5)
		request.session['activity'].append({'color': 'green','text': "Earned {} golds from the {}! ({})".format(earned,'house',strftime("%Y/%m/%d %I:%M %p"))})
		request.session['gold'] += earned
	return redirect('/')
def casino(request):
	if request.method == 'POST':
		earned = randint(-50,50)
		if earned > 0:
			request.session['activity'].append({'color': 'green','text': "Earned {} golds from the {}! ({})".format(earned,'Casino',strftime("%Y/%m/%d %I:%M %p"))})
		else:
			request.session['activity'].append({'color': 'red','text': "Entered a casino and lost {} golds...Ouch... ({})".format(0-earned,strftime("%Y/%m/%d %I:%M %p"))})
		request.session['gold'] += earned
	return redirect('/')
		