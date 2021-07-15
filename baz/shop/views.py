from django.shortcuts import render
from .models import Product
# from django.http import HttpResponse

def index(request):
    products=Product.objects.all()
    print(products)
    params={}
    # return HttpResponse("Index Shop")
    return render(request, 'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def product(request):
    return render(request,'product.html')

def search(request):
    return render(request,'search.html')

# Create your views here.
