from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index),
	url(r'^tiem_display$',views.index)
] 