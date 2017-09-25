# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PostManager(models.Manager):
	def post_validator(self,postData):
		error = {}
		if len(postData['content'])<5:
			error['content'] = "the note should be at least 5 characters"
		return error

class Post(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PostManager()
	def __str__(self):
		return "<Post Object {}>".format(self.content)