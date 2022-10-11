from django.shortcuts import render


def index(request):
    return render(request, 'main/layout.html',)


def contactme(request):
    return render(request, 'main/contactme.html')


def expireance(request):
    return render(request, 'main/expireance.html')

def home(request):
    return render(request, 'main/home.html')