from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import datetime
from main.forms import ProductEntryForm
from main.models import Product

# Create your views here.
@login_required(login_url='/login')
def frontpage(request):
    products = Product.objects.filter(user=request.user)[0:4]
    last_login = request.COOKIES.get('last_login', 'Unknown')
    context = {
        'products': products,
        'last_login': last_login,
        'name': request.user.username,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:frontpage')
    
    context = {'form': form}
    return render(request, 'product_entry.html', context)


# DATA
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


# AUTENTIFIKASI
def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('main:login')
    
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