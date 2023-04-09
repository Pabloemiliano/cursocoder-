from django.db import models
from django.contrib.auth.models import User

class Problema(models.Model):
    materiaSeleccion = (
    ('matematica','Matematica'),
    ('fisica','Fisica'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    materia = models.CharField(max_length=15, choices=materiaSeleccion, default='matematica')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.CharField(max_length=4) 
    precio = models.CharField(max_length=5)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenInstrumento = models.ImageField(null=True, blank=True, upload_to="imagenes/")


    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Problema, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)