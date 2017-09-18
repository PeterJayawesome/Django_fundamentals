from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.survey_form),
	url(r'^survey/process', views.process),
	url(r'^result$', views.result)
]