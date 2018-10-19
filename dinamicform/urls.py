from django.conf.urls import url
import dinamicform.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^done/$', views.done),
]
