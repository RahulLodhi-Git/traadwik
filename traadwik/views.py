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