from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from .models import Item
import pandas as pd
import logging
from django.contrib.auth.decorators import login_required



logger = logging.getLogger(__name__)

def get_item_details(request, item_id):
    item = Item.objects.get(id=item_id)
    data = {
        'id': item.id,
        'item': item.item,
        'description': item.description
    }
    return JsonResponse(data)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        logger.debug('This is a debug message')
        if user is not None:
            auth_login(request, user)

            return redirect('welcome')
        else:
            # Handle invalid login credentials (e.g., show an error message)
            pass
    return render(request, 'login.html')

@login_required
def welcome(request):
    # return render(request, 'welcome.html', {'username': [username]})
    items = Item.objects.all()  # Assuming you have a model named Item
    first_name = request.user.first_name
    # Sample data
    data = {
        'Name': ['John', 'Alice', 'Bob', 'Jane'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    data = df.to_dict('records')
    return render(request, 'welcome.html', {'username': first_name, 'items': items, 'data': data})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def edit(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    if request.method == 'POST':
        # Handle form submission and save changes to database
        # You can use a Django form for validation and saving data
        # Here's a basic example without form validation for simplicity
        item.item = request.POST.get('item')
        item.description = request.POST.get('description')
        item.save()
        # Redirect to some success page or back to the welcome page
        return redirect('welcome')
    return render(request, 'edit.html', {'item': item})

@login_required
def delete(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    # if request.method == 'POST':
    item.delete()
    # Redirect to some success page or back to the welcome page
    return redirect('welcome')
    # return render(request, 'edit.html', {'item': item})

@login_required
def add_item(request):
    if request.method == 'POST':
        # Handle form submission and save new item to database
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        item = Item.objects.create(item=item_name, description=description)
        return redirect('welcome')
    return render(request, 'add_item.html')