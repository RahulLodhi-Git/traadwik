import re
from django.shortcuts import render;


def index(request):
    return render(request,'index.html')

# contact
def contact(request):
    return render(request,'contact.html')

# About
def about(request):
    return render(request,'about.html')

def careers(request):
    return render(request, 'careers.html')

# Price List
def priceList(request):
    return render(request,'price-list.html')


# Product-detail
def productDetail(request,slug):
    productName=slug.replace("-", " ").capitalize()
    return render(request,'product-detail.html',{'slug':productName})

# Search
def search(request):
    if 'search-query' in request.GET:
        query = 'You searched for: %r' % request.GET['search-query']
    else:
        query = 'You submitted an empty form.'
    print(query)
    return render(request,'search.html',{'query':query})
    