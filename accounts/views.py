from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User
from autor.models import Autor


def add_user(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.email = u.username
            u.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
                
        else:
            print(form.errors)
            messages.error(request, form.errors)
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', locals())


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            print(messages.error)
            messages.error(request, 'Usuário ou senha inválido ou desativado.')
    return render(request, 'accounts/login.html')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, f'{form.errors}')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/alterar_senha.html', locals())

@login_required
def editar_user(request):
    usuario = User.objects.get(id=request.user.id)
    if request.method == 'POST':     
        form = UserForm(data=request.POST, instance=usuario)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect(request.GET.get('next', '/'))
        else:
            print(form.errors)
    else:
        form = UserForm(instance=usuario)
    return render(request, 'accounts/editar_user.html', locals())


def user_logout(request):
    logout(request)
    return redirect(request.GET.get('next','/'))
