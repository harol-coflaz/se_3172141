# Vistas para la navegación general del aplicativo

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'se_core/index.html')
def acerca_de(request):
    return render(request, 'se_core/acercade.html')
def mision_vision(request):
    return render(request, 'se_core/misionvision.html')
def contáctanos(request):
    return render(request, 'se_core/contáctanos.html')
def inicio_sesion(request):
    return render(request, 'se_core/inicio_frm.html')
def loginn(request):
    correo = request.POST.get('correo')
    clave = request.POST.get('clave')

    if correo == "juanpablocuitiva@gmail.com" and clave == "12345":
        return HttpResponse(f"Correo: {correo}, Clave: {clave}")
    else:
        mensaje = "*Datos no válidos*"
        return render(request, 'se_core/inicio_frm.html', contexto)