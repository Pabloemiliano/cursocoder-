from django import views
from django.urls import path
from Colegio.views import *
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='colegio/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaMatematica/', MatematicaLista.as_view(), name='matematicas'),
    path('listaFisica/', FisicaLista.as_view(), name='fisicas'),
    
    path('matematicaDetalle/<int:pk>/', MatematicaDetalle.as_view(), name='matematica'),
    path('fisicaDetalle/<int:pk>/', FisicaDetalle.as_view(), name='fisica'),
    
    path('matematicaEdicion/<int:pk>/', MatematicaUpdate.as_view(), name='matematica_editar'),
    path('fisicaEdicion/<int:pk>/', FisicaUpdate.as_view(), name='fisica_editar'),
    
    path('matematicaBorrado/<int:pk>/', MatematicaDelete.as_view(), name='matematica_eliminar'),
    path('fisicaBorrado/<int:pk>/', FisicaDelete.as_view(), name='fisica_eliminar'),
    
    path('ProblemaCreacion/', ProblemaCreacion.as_view(), name='nuevo'),

    path('matematicaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('fisicaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    
    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]