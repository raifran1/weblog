from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.shortcuts import get_object_or_404 

#decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#model Autor
from .models import Postagem
from .forms import PostagemForm
from autor.models import Autor

@login_required
def cadastro_post(request):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect(request.GET.get('next', '/'))
        else:
            print(form.errors)
    else:
        form = PostagemForm()
    data = datetime.now()
    return render(request, 'postagem/postar.html', locals())

def posts(request):
    posts = Postagem.objects.filter(status='Publicado')
    return render(request, 'postagem/posts.html', locals())

def posts_autor(request):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    posts = Postagem.objects.filter(autor=autor)
    return render(request, 'postagem/postagens_autor.html', locals())

def deletar_post(request,id_post):
    posts = get_object_or_404(Postagem, id=id_post)
    posts.delete()
    return redirect(request.GET.get('next', '/postagens/autor/'))

def editar_post(request,id_post):
    usuario = User.objects.get(id=request.user.id)
    autor = Autor.objects.get(email=usuario.email)
    post = Postagem.objects.get(id=id_post)

    if request.method == 'POST':
        form = PostagemForm(data=request.POST, instance=post)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect(request.GET.get('next', '/postagens/autor/'))
        else:
            print(form.errors)
    else:
        form = PostagemForm(instance=post)
    data = datetime.now()
    return render(request, 'postagem/editar_post.html', locals())
