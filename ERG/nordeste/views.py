from django.shortcuts import render

def index(request):
    return render(request, 'nordeste/index.html')

def pe(request):
    return render(request, 'nordeste/paises/pernambuco.html')

def rn(request):
    return render(request, 'nordeste/paises/rio_grande_do_norte.html')