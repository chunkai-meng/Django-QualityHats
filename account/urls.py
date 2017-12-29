from django.conf.urls import url
from django.views.generic import ListView
from django.contrib.auth.models import User
from account import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userdetail/$', views.userdetail, name='userdetail'),
    url(r'^userlist/$', ListView.as_view(model=User), name='userlist'),
]
