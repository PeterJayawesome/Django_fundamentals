# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# Create your models here.
NAME_REGEX = re.compile(r'^[A-Za-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALIAS_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
class UserManager(models.Manager):
	def reg_validator(self,postData):
		errors = {}
		if "name" not in postData or not NAME_REGEX.match(postData['name']):
			errors['name'] = "Please enter a valid name"
		if "alias" not in postData or not ALIAS_REGEX.match(postData['alias']):
			errors['alias'] = "Please enter a valid alias"
		if "email" not in postData or not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Please enter a valid email"
		if 'password' not in postData or len(postData['password'])<8:
			errors['password'] = "Password must have at least 8 characters"
		elif "confirm" not in postData or postData['password'] != postData['confirm']:
			errors['password'] = "Please enter your password again"
		if not len(errors):
			users = User.objects.filter(email = postData['email'])
			if users:
				errors['email'] = "Please enter a valid email"
		return errors
	def login_check(self,postData):
		error = {}
		users = User.objects.filter(email = postData['email'])
		if not users or not bcrypt.checkpw(postData['password'].encode(),users[0].password.encode()):
			error['login'] = "Email and password not match"
		return error
class BookManager(models.Manager):
	def book_duplicate_validator(self,postData):
		books = Book.objects.filter(title__iexact=postData['title'])
		if postData['author'] in [book.author for book in books]:
			return True
		else:
			return False
		#check if the book exist in db
class AuthorManager(models.Manager):
	def new_author_validator(self,postData):
		authors = Author.objects.filter(name__iexact=postData['new_author'])
		if authors:
			return authors[0]
		else:
			return False
	# if the author is not in the author table, return false;
	# if the author in the db, return the value in db
class ReviewManager(models.Manager):
	def review_validator(self,postData):
		error = {}
		if len(postData['review'])<5:
			error['review'] = "The review should be at least 5 characters"
		return error

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def __str__(self):
		return "<User object {} {} {}".format(self.name, self.alias,self.email)

class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = AuthorManager()
	def __str__(self):
		return "<Author object {}".format(self.name)
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author,related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()
	def __str__(self):
		return "<Book object {}".format(self.title)
class Review(models.Model):
	rating = models.IntegerField()
	review = models.TextField()
	user = models.ForeignKey(User,related_name="reviews")
	book = models.ForeignKey(Book,related_name="reviews")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()
	def __str__(self):
		return "<Review object {} {}".format(self.rating,self.user.name)
