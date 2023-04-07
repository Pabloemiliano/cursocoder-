from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context
from django.template import loader

def saludo(Request):
    return HttpResponse("Hola Django")

def segunda(Request):
    return HttpResponse("Segunda vista")

def dia(Request):
    hoy = dt.now()
    return HttpResponse(f"Hoy es:<br>{hoy}")

def mostrarnombre(Request, nombre):
    texto = f"Tu nombre es: {nombre}"
    return HttpResponse(texto)

def probandoTemplate(Request):
    
    nom = "Pablo"
    apellido = "Lopez"
    notas = [9,5,5,10,9]
    dictemplate = {"nombre": nom, "apellido" : apellido, "notas": notas}

   # mihtml = open('./template/template1.html')
   # plantilla = Template(mihtml.read())
   # mihtml.close()
    plantilla = loader.get_template("template1.html")

   # mi_contexto = Context(dictemplate)

    documento = plantilla.render(dictemplate)
    return HttpResponse(documento)

