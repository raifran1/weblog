from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

#decorators
from django.contrib.auth.decorators import login_required

#model Autor
from .models import Autor
from .forms import AutorForm

#conta de usuario
from django.contrib.auth.models import User

def cadastro_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return HttpResponseRedirect(reverse('accounts:add_user', args=(f.id, )))
        else:
            print(form.errors)
    else:
        form = AutorForm()
    return render(request, 'autor/cadastrar_autor.html', locals())


@login_required
def editar_autor(request):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    if request.method == 'POST':
        form = AutorForm(data=request.POST, instance=autor)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect(request.GET.get('next', '/'))
        else:
            print(form.errors)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/editar_autor.html', locals())
