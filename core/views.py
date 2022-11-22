from django.shortcuts import render
from .models import Hoodie, Hoodie1, Hoodie2, Hoodie3, Hoodie4

def Hoodie(request):
    malumotlar = Hoodie.objects.all()
    qolip = {
        "malumot": malumotlar
    }


    return render(request, "hoodie.html", qolip)

def Hoodie1(request):
    malumotlar1 = Hoodie1.objects.all()
    qolip1 = {
        'malumotlar1': malumotlar1
    }
    return render(request, 'Hoodie1.html', qolip1)


def Hoodie2(request):
    malumotlar2 = Hoodie2.objects.all()
    qolip2 = {
        'malumotlar2': malumotlar2
    }
    return render(request, 'Hoodie2.html', qolip2)

def Hoodie3(request):
    malumotlar3 = Hoodie3.objects.all()
    qolip3 = {
        'malumotlar3': malumotlar3
    }
    return render(request, 'Hoodie3.html', qolip3)

def Hoodie4(request):
    malumotlar4 = Hoodie4.objects.all()
    qolip4 = {
        'malumotlar4': malumotlar4
    }
    return render(request, 'Hoodie4.html', qolip4)



