from django.urls import path
from . import views

app_name = 'order_app'
url_patterns = [
    path(r'^$', views.OrderListView.as_view(), name='list'),
    path(r'^(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='detail'),
    path(r'^create/$', views.OrderCreateView.as_view(), name='create'),
    path(r'update/(?P<pk>\d+)/$', views.OrderUpdateView.as_view(), name='update'),
    path(r'delete/(?P<pk>\d+)/$', views.OrderDeleteView.as_view(), name='delete'),
]
