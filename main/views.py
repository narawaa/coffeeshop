from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:4]
    return render(request, 'main.html', {'products': products})

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:frontpage')
    
    context = {'form': form}
    return render(request, 'product_entry.html', context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")