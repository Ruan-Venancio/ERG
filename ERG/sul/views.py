from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sul/index.html')

def sc(request):
    return render(request, 'sul/paises/santa_catarina.html')

def pr(request):
    return render(request, 'sul/paises/parana.html')

def rs(request):
    return render(request, 'sul/paises/rio_grande_do_sul.html')