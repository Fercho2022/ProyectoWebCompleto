from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render (request, "ProyectoWebCompletoApp/home.html")


def servicios(request):

    return render (request, "ProyectoWebCompletoApp/servicios.html")


def tienda(request):

    return render (request, "ProyectoWebCompletoApp/tienda.html")


def blog(request):

    return render (request, "ProyectoWebCompletoApp/blog.html")


def contacto(request):

    return render (request, "ProyectoWebCompletoApp/contacto.html")  