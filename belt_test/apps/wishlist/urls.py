from django.conf.urls import url
import views

urlpatterns=[
	url(r'^main$',views.main),
	url(r'^dashboard$',views.dashboard),
	url(r'^wish_items/(?P<id>\d+$',views.item),
	url(r'^wish_items/create$',views.add_item),
	url(r'^main/login$',views.login),
	url(r'^main/reg$',views.reg),
	url(r'^wish_items/remove$',views.remove),
	url(r'^wish_items/delete$',views.delete),
	url(r'^wish_items/add$',views.add),
	url(r'^wish_items/create/confirm$',views.create),
]