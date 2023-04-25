from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import UserModel
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home.html')


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'error_message': 'Invalid login'})
    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_delete(request, user_id):
    try:
        user = UserModel.objects.get(id=user_id)
        user.delete()
        return True, "Пользователь успешно удален."
    except UserModel.DoesNotExist:
        return False, "Пользователь с указанным ID не найден."


