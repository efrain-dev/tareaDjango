from django.shortcuts import render

# Create your views here.
def formulario1(request):
    return render(request, 'form1.html')


def formulario2(request):
    return render(request, 'form2.html')


def formulario3(request):
    return render(request, 'form3.html')


def formulario4(request):
    return render(request, 'form4.html')


def formulario5(request):
    return render(request, 'form5.html')


def home(request):
    return render(request, "home.html")
