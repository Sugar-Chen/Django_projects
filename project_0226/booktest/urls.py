from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^login$',views.login),
    url(r'^books$',views.show_book),
    url(r'^books/(\d+)$',views.detail)
]
