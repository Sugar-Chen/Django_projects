from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^myfilter$', views.myfilter),
    url(r'^block$', views.block),
    url(r'^login$', views.login),
    url(r'^logincheck$', views.logincheck),
    url(r'^changepwd$', views.changepwd),
    url(r'^changeover$', views.changeover),
]
