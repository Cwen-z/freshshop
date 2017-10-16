from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register,name='register'),
    url(r'^register_handler/$', views.register_handler),
    url(r'^register_exist/$',views.register_exist),
    url(r'^login/$', views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^center_info/$', views.center_info,name="center_info"),
    url(r'^center_site/$', views.center_site,name="center_site"),
    url(r'^pro_id/(\d*)$', views.pro_id),
    url(r'^address_handler/(\d*)$', views.address_handler, name='address_handler'),
    url(r'^editor/(\d*)$',views.editor),
    url(r'^del_address/(\d*)$',views.del_address),
]