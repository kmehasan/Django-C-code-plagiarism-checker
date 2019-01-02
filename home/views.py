from django.shortcuts import render


def index (request):
    return render(request, 'home/login.html')

def home(request):
    return render(request, 'home/homepage.html')


def physics(request):
    return render(request, 'home/physics.html')


def chemistry(request):
    return render(request, 'home/chemistry.html')


def mathematics(request):
    return render(request, 'home/mathematics.html')
