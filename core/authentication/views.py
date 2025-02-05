# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from .models import *
from .forms import PasswordVerificationForm

@login_required
def home(request):
    users = User.objects.all()
    context = {
        'users': users,
        'user': request.user,
        'user_is_authenticated': request.user.is_authenticated
    }
    return render(request, 'home.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Usuario no encontrado')
            return redirect('signin')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Contraseña incorrecta")
            return redirect('signin')
        else:
            login(request, user)
            return redirect('home')
    
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está registrado")
            return redirect('signup')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.save()
        
        messages.info(request, "Usuario registrado con éxito")
        return redirect('/signin/')
    
    else:
        context = {'user_is_authenticated': request.user.is_authenticated}
        return render(request, 'register.html', context)

@login_required
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST['username']
        user.save()
        messages.success(request, 'Usuario actualizado con éxito')
        return redirect('home')
    return render(request, 'edit_user.html', {'user': user, 'user_is_authenticated': request.user.is_authenticated})

@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = PasswordVerificationForm(request.user, request.POST)
        if form.is_valid():
            user.delete()
            messages.success(request, 'Usuario eliminado con éxito')
            return redirect('signin')
        else:
            messages.error(request, 'Contraseña incorrecta')
            return redirect('delete_user', user_id=user_id)
    else:
        form = PasswordVerificationForm(request.user)
        context = {
            'user': user,
            'form': form,
            'user_is_authenticated': request.user.is_authenticated
        }
        return render(request, 'delete_user.html', context)

def admin_check(user, login_url='access_denied'):
    print(user.groups)
    return user.groups.filter(name='administrador').exists()


@user_passes_test(admin_check)
@login_required
def admin_page(request):
    context = {
        'user_is_authenticated': request.user.is_authenticated,
        'user': request
    }
    return render(request, 'admin/admin.html', context)

@login_required
def access_denied(request):
    context = {
        'user_is_authenticated': request.user.is_authenticated,
        'user': request
    }
    return render(request, 'access_denied.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('signin')