from django.shortcuts import render
from django.http import HttpResponse
from Colegio.forms import *
from Colegio.models import Curso

# Create your views here.
def inicio (request):
    return HttpResponse("esta es la pagina de inicio")

def index (request):
    return render(request,'Colegio/index.html')

def padre (request):
    return render(request, 'Colegio/padre.html')

def curso (request):
    return render(request,'Colegio/curso.html')

def estudiante (request):
    return render(request,'Colegio/estudiante.html')

def examen (request):
    return render(request,'Colegio/examen.html')

def profesor (request):
    return render(request,'Colegio/profesor.html')

def GuardaCursoform(request):
    

        if request.method == "POST":
            print(f"\n\n{request.POST}\n\n")
            nombre = request.POST["curso"]
            camada = request.POST["camada"]
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()

        return render(request, "Colegio/cursoformulario.html")  

def Guardacurso(request):


    if request.method == "POST":
       miFormulario = BuscarCursoform(request.POST)
       print(miFormulario)
       if miFormulario.is_valid():
           informacion = miFormulario.cleaned_data
           curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
           curso.save()
       return render(request,"Colegio/index.html")
    else:
        miFormulario = BuscarCursoform()
    return render(request, "Colegio/guardacurso.html", {"miFormulario":miFormulario})  


def Buscar_camada(request):
    return render(request, "Colegio/buscarcamada.html") 
    
def Buscar(request):    
    if request.method == "POST":
        camada = request.POST["camada"]
        cursos = Curso.objects.filter(camada = camada)
        
        return render(request,"Colegio/mostrarbusqueda.html", {"cursos":cursos, "camada":camada} )
    else:
        respuesta = "no hay info"
    return HttpResponse(respuesta)  