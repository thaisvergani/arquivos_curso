from django.conf.urls import url
from . import views

urlpatterns = [
    # home page of products app /products/
    url(r'^$', views.index, name='index'),

    # /products/123/
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail')
]
