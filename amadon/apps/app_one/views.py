# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
item_list = [
	{'name': 'Dojo Tshirt', 'price': 19.99},
	{'name': 'Dojo Sweater', 'price': 29.99},
	{'name': 'Dojo Cup', 'price': 4.99},
	{'name': 'Algorithm Book', 'price': 49.99}
]
# Create your views here.
def amadon(request):
	if 'order_history' not in request.session:
		request.session['order_history'] = {'amount': 0, 'spend': 0.0}
	return render(request,'app_one/amadon.html')
def checkout(request):
	return render(request,'app_one/checkout.html')
def buy(request):
	if request.method == 'POST':
		request.session['checkout'] = []
		request.session['checkout'].append({'item_id': request.POST['item_id'], 'amount': request.POST['amount']})
		request.session['order_summary'] = item_list[int(request.POST['item_id'])]['price']*int(request.POST['amount'])
		request.session['order_history']['spend'] += request.session['order_summary']
		request.session['order_history']['amount'] += int(request.POST['amount'])
		return redirect('/amadon/checkout')
	return redirect('/amadon')