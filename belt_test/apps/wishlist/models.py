# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def reg_validator(self,postData):
		errors = {}
		if "name" not in postData or len(postData['name'])<3:
			errors['name'] = "Please enter a valid name"
		if "username" not in postData or len(postData['username'])<3:
			errors['username'] = "Please enter a valid username"
		if "date" not in postData:
			errors['date'] = "Please enter date hired"
		if 'password' not in postData or len(postData['password'])<8:
			errors['password'] = "Password must have at least 8 characters"
		elif "confirm" not in postData or postData['password'] != postData['confirm']:
			errors['password'] = "Please enter your password again"
		if not len(errors):
			users = User.objects.filter(username = postData['username'])
			if users:
				errors['username'] = "Please change a username"
		return errors
	def login_check(self,postData):
		error = {}
		users = User.objects.filter(username = postData['username'])
		if not users or not bcrypt.checkpw(postData['password'].encode(),users[0].password.encode()):
			error['login'] = "Email and password not match"
		return error
class ItemManager(models.Manager):
	def add_item_validator(self,postData):
		errors = {}
		if 'item' not in postData or len(postData['item'])<3:
			errors['item'] = "Please enter a valid item/porduct name"
		if not len(errors):
			items = Item.objects.filter(item=postData['item'])
			if items:
				errors['item'] = "This item has been added before" 
		return errors
class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	date_hired = models.DateTimeField()
	created_at = models.DateTimeField(auto_add_now=True)
	updated_at = models.DateTimeField(auto_add=True)
	objects = UserManager()
	def __str__(self):
		return "<User: object {} {}".format(self.name, self.username)

class Item(models.Model):
	item = models.CharField(max_length=255)
	added_by = models.ForeignKey(User, related_name="added_items")
	wished_by = models.ManyToManyField(User,related_name="wish_list")
	created_at = models.DateTimeField(auto_add_now=True)
	updated_at = models.DateTimeField(auto_add=True)
	objects = 
	def __str__(self):
		return "<Item: object {}".format(self.item)