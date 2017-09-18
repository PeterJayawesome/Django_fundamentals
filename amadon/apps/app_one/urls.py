from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.amadon),
	url(r'^checkout$',views.checkout),
	url(r'^buy$',views.buy),
]