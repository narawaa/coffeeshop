from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags

import datetime
from main.forms import ProductEntryForm
from main.models import Product

# PAGE
@login_required(login_url='/login')
def frontpage(request):
    # products = Product.objects.filter(user=request.user)[0:4]
    last_login = request.COOKIES.get('last_login', 'Unknown')
    context = {
        # 'products': products,
        'last_login': last_login,
        'name': request.user.username,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:frontpage')
    
    context = {'form': form}
    return render(request, 'product_entry.html', context)


# METHOD
def edit_product(request, id):
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:frontpage'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:frontpage'))


# DATA
def show_xml(request):
    data = Product.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# AUTENTIFIKASI
def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('main:login')
        
        else:
            print(form.errors)
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    
    context = {'form': form}
    return render(request, 'signup.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:frontpage"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            messages.success(request, 'Logged in successfully')
            return response
        
        else:
            messages.error(request, 'Please enter a correct username and password.')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.success(request, 'Logged out successfully')
    return response


# AJAX
@csrf_exempt
@require_POST
def create_ajax(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')
    stock = request.POST.get('stock')
    user = request.user

    if name != strip_tags(name) or description != strip_tags(description):
        return HttpResponse('HTML tags are not allowed', status=400)

    new_product = Product(
        name = name,
        price = price,
        description = description,
        stock = stock,
        user = user,
    )
    new_product.save()
    return HttpResponse(status=201)
