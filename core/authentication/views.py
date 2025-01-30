# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def home(request, user_id):
    user = User.objects.get(id=user_id)
    users = User.objects.all()
    context = {
        'user': user,
        'users': users
    }
    return render(request, 'home.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Usuario no encontrado')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Contraseña incorrecta")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, "Usuario ya registrado")
            return redirect('/register/')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        user.set_password(password)
        user.save()
        
        messages.info(request, "Usuario registrado con éxito")
        return redirect('/register/')
    
    return render(request, 'register.html')

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST['username']
        user.save()
        messages.success(request, 'Usuario actualizado con éxito')
        return redirect('home')
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado con éxito')
        return redirect('home')
    return render(request, 'delete_user.html', {'user': user})