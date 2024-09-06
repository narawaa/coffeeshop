from django.shortcuts import render
from .models import Product

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:4]
    return render(request, 'main.html', {'products': products})