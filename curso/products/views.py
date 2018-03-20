# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product
# Create your views here.

###### 1
# def index(request):
#
#     return HttpResponse('<h1>Products homepage</h1>')

###### 2
# def index(request):
#     html = ''
#     all_products = Product.objects.all()
#     for product in all_products:
#         url = '/product/{prod_id}'.format(prod_id=product.id)
#         html += '<a href="{id}">{name}</a><br>'.format(
#             id=product.id,
#             name=product.name)
#     return HttpResponse(html)
#

###### 4
# def index(request):
#     all_products = Product.objects.all()
#     template = loader.get_template('products/index.html')
#     context = {
#         'all_products': all_products
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    all_products = Product.objects.all()
    context = {
        'all_products': all_products
    }
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    try:
        product =  Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('o produto não existe')
    return HttpResponse('Detalhes do produto' + product_id)
