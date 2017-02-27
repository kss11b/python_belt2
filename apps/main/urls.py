from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^success$', views.success),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^new_app$',views.new_app),
    url(r'^update_page/(?P<id>\d+)$', views.update_page),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^logout$', views.logout)



]
