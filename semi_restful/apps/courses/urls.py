from django.conf.urls import url
import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^add$',views.add),
	url(r'^(?P<id>\d+)/destory$',views.delete),
	url(r'^(?P<id>\d+)/comments$',views.comments),
	url(r'^(?P<id>\d+)/destory/confirm$',views.remove),
	url(r'^(?P<id>\d+)/comments/create$',views.create),
]