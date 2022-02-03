from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def hola(request):
    return HttpResponse("hola")

def saludar(request):
    return HttpResponse("saludar")

def saludar_nombre(request, nombre):
    return HttpResponse("saludar a "+ nombre)    

def aumenta(request, cantidad):
    return HttpResponse(f"aumentando en 10: { cantidad + 10 }")    

def editar(request, id):
    return HttpResponse(f" editando el id del usuario : {id}")  

def template_uno (request):

    apellido = 'Boisier'

    contexto = {
        'nombre' : 'Francisco',
        'apellido' : apellido
    }

    return render(request, 'app/main.html', contexto)