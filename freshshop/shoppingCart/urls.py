# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.cart,name='cart'),
    url(r'^add_cart/(\d+)_(\d+)$',views.add_cart,name='add_cart'),
    url(r'^cart_nums/$',views.cart_nums),
    url(r'^cart_edit/(\d+)_(\d+)$',views.cart_edit),
    url(r'^del_cart_(\d+)$',views.del_cart),
]