from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^myfilter$', views.myfilter),
    url(r'^block$', views.block),
    url(r'^login$', views.login),
    url(r'^logincheck$', views.logincheck),
    url(r'^changepwd$', views.changepwd),
    url(r'^changeover$', views.changeover),
    url(r'^upload$', views.upload),
    url(r'^upload_handle$', views.upload_handle),
    url(r'^show_area/(?P<page_num>\d*)$', views.show_area),
]
