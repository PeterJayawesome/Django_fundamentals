from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^login$',views.login),
	url(r'^register$',views.register),
	url(r'^books$',views.books),
	url(r'^books/add$',views.add),
	url(r'^books/(?P<book_id>\d+)$',views.review),
	url(r'^user/(?P<user_id>\d+)$',views.user),
	url(r'^create$',views.create),
	url(r'^books/(?P<book_id>\d+)/review$',views.write_review),
	url(r'^books/(?P<book_id>\d+)/(?P<review_id>\d+)/delete$',views.delete_review),
]