from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.random_word),
	url(r'^reset$',views.reset),
]