from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$',views.posts),
	url(r'^add_note$',views.add_note),
]