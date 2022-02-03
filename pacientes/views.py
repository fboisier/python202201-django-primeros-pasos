from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("YO SOY DEL PACIENTE INDEX")

def listado(request):
    return render(request, "pacientes/listado.html")