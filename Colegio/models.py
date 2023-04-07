from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} - {self.nombre} - {self.camada}"
class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self) -> str:
        return f"{self.id} - {self.nombre}  {self.apellido}"
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    materia = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.id} - {self.nombre}  {self.apellido} - {self.materia}"
class Examen(models.Model):

    materia = models.CharField(max_length=50)
    fecha = models.DateField()
    nota = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} - {self.materia} - {self.fecha} - {self.nota}"

