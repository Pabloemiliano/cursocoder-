from django.urls import path
from Colegio.views import *


urlpatterns = [
    path('', index, name="index"),
    path('curso/', curso, name="curso"),
    path('estudiante/', estudiante, name="estudiante"),
    path('examen/', examen, name="examen"),
    path('profesor/', profesor, name="profesor"),
    path('guarda-curso/', GuardaCursoform, name="GuardaCursoForm"),
    path('guardacurso/', Guardacurso, name="GuardaCurso"),
    path('buscarcamada/', Buscar_camada, name="Buscar_camada"),
    path('buscar/', Buscar, name="Buscar"),
     path('mostrarbusqueda/', Buscar, name="mostrar busqueda"),
    ]


#urlpatterns = [
 #   path('', index, name="index"),
  #  path('curso/', curso, name="curso"),
   # path('estudiante/', estudiante, name="estudiante"),
 #   path('examen/', examen, name="examen"),
  #  path('profesor/', profesor, name="profesor"),
 #   path('guarda-curso/', GuardaCursoform, name="GuardaCursoform"),
  #  path('guardacurso/', Guardacurso, name="GuardaCurso"),
#]
