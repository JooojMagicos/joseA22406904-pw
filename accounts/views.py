from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio:index')
        else:
            erro = 'Utilizador ou palavra-passe incorretos.'
    return render(request, 'accounts/login.html', {'erro':erro})

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('portfolio:index')

def register_View(request):
    form = RegisterForm()
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                 form.save()
                 return redirect('accounts:login')
    return render(request,'accounts/register.html', {'form': form})