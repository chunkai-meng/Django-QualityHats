from django.urls import path
from django.views.generic import ListView
from django.contrib.auth.models import User
from account import views

app_name = 'account'
urlpatterns = [
    path(r'^$', views.IndexView.as_view(), name='index'),
    path(r'^register/$', views.register, name='register'),
    path(r'^login/$', views.login, name='login'),
    path(r'^logout/$', views.logout, name='logout'),
    path(r'^userdetail/$', views.userdetail, name='userdetail'),
    path(r'^userlist/$', ListView.as_view(model=User), name='userlist'),
]
