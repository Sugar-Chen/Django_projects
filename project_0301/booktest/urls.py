from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logincheck$', views.logincheck),
    url(r'^ajax_test$', views.ajax_test),
    url(r'^ajax_handel$', views.ajax_handel),
    url(r'^ajax_login$', views.ajax_login),
    url(r'^ajax_login_check$', views.ajax_login_check)
]
