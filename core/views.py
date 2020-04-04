from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/base_principal.html')

def contato(request):
    return render(request, 'core/contato.html')
