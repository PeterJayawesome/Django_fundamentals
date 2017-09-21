# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
from models import*
import bcrypt
# Create your views here.
def index(request):
	request.session['log'] = False
	return render(request,"reviewer/log.html")
def login(request):
	if request.method == "POST":
		request.session['log_reg'] = 'log'
		error = User.objects.login_check(request.POST)
		if len(error):
			messages.error(request,"Email and password not match",extra_tags="login")
			return redirect('/')
		else:
			request.session['log'] = True
			request.session['user_id'] = User.objects.get(email = request.POST['email']).id
			return redirect('/books')
	return redirect('/')
def register(request):
	if request.method == "POST":
		request.session['log_reg']='reg'
		errors = User.objects.reg_validator(request.POST)
		if len(errors):
			for tag,error in errors.iteritems():
				messages.error(request,error,extra_tags=tag)
			return redirect('/')
		secure_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
		User.objects.create(name=request.POST['name'],alias = request.POST['alias'],email = request.POST['email'],password = secure_password)
		request.session['log'] = True
		request.session['user_id'] = User.objects.last().id
		return redirect('/books')
	return redirect('/')
def books(request):
	if "log" in request.session and request.session['log']:
		user = User.objects.get(id=request.session['user_id'])
		reviews = Review.objects.all().order_by('-created_at')[:3]
		books = Book.objects.exclude(id__in=[review.book.id for review in reviews])
		context = {
			'user': user,
			'reviews': reviews,
			'books': books
		}
		return render(request,"reviewer/book.html",context)
	return redirect('/')
def add(request):
	if "log" in request.session and request.session['log']:
		context={"authors": Author.objects.all()}
		return render(request,"reviewer/add.html",context)
	return redirect('/')
	
def review(request,book_id):
	books = Book.objects.filter(id=book_id)
	if books:
		reviews = books[0].reviews.all().order_by('-updated_at')
		context = {
			"book": books[0],
			"reviews": reviews 
		}
		return render(request,"reviewer/review.html",context)
	return redirect('/books')
def user(request,user_id):
	users=User.objects.filter(id = user_id)
	if users:
		# select all books this user writed a review on:(duplicate books?)
		books = [review.book for review in users[0].reviews.all()]
		count = users[0].reviews.count()
		context={
			"user": users[0],
			"count": count,
			"books": books
		}
		return render(request,"reviewer/user.html",context)
	return redirect('/books')
def create(request):# can have a validator here
	if request.method == "POST":
		error = Review.objects.review_validator(request.POST)
		if len(error):
			messages.error(request,error['review'],extra_tags="review")
			return redirect('/books/add')
		if "new_author" in request.POST:
			author = Author.objects.new_author_validator(request.POST)
			if author:
				postData = {"author": author, "title": request.POST['title']}
				if Book.objects.book_duplicate_validator(postData):
					messages.error(request,"This book has been added before",extra_tags="book")
					return redirect('/books/add')
			else:
				Author.objects.create(name = request.POST['new_author'])
				author = Author.objects.last()
		elif Book.objects.book_duplicate_validator(request.POST):
			messages.error(request,"This book has been added before",extra_tags="book")
			return redirect('/books/add')
		else:
			author = Author.objects.get(name = request.POST['author'])
		Book.objects.create(title=request.POST['title'],author=author)
		Review.objects.create(rating=request.POST['rating'],
			review=request.POST['review'],
			book=Book.objects.last(),
			user=User.objects.get(id=request.session['user_id']))
		return redirect("/books/"+str(Book.objects.last().id))
	return redirect("/books/add")
def write_review(request,book_id):# could have a validator here
	if request.method == "POST":
		error = Review.objects.review_validator(request.POST)
		if len(error):
			messages.error(request,error['review'],extra_tags="review")
			return redirect("/books/"+book_id)
		Review.objects.create(rating=request.POST['rating'],
				review=request.POST['review'],
				book=Book.objects.get(id=book_id),
				user=User.objects.get(id=request.session['user_id']))
	return redirect("/books/"+book_id)
def delete_review(request,book_id,review_id):
	review = Review.objects.get(id = review_id)
	
	if request.session['user_id'] == review.user.id and review.book.id == int(book_id):
		review.delete()
		if not Book.objects.get(id=book_id).reviews.all():
			book = Book.objects.get(id=book_id)
			book.delete()
			return redirect('/books')
	return redirect('/books/'+book_id)
