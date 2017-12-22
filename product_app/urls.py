from django.conf.urls import url
from . import views

app_name = 'product_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_hat/$', views.add_hat, name='add_hat'),
    url(r'^test/(\d{4})/(\d{2})', views.test, name='test'),
]
