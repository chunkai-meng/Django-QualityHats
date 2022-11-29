from django.urls import path
from . import views

app_name = 'product_app'

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^add_hat/$', views.add_hat, name='add_hat'),
    path(r'^test/(\d{4})/(\d{2})', views.test, name='test'),
]
