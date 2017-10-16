from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^goods/(\d+)$',views.detail,name='detail'),
    url(r'^goods/(\d+)/(\d+)/(\d+)$',views.good_list,name='list')
]