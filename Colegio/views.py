from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from Colegio.models import Problema, Comentario
from Colegio.forms import ActualizacionProblema, FormularioCambioPassword, FormularioEdicion, FormularioNuevoProblema, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'Colegio/home.html'

class LoginPagina(LoginView):
    template_name = 'colegio/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'colegio/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'colegio/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'Colegio/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'colegio/passwordExitoso.html', {})



class MatematicaLista(LoginRequiredMixin, ListView):
    context_object_name = 'matematicas'
    queryset = Problema.objects.filter(materia__startswith='matematica')
    template_name = 'Colegio/listaMatematica.html'
    login_url = '/login/'

class MatematicaDetalle(LoginRequiredMixin, DetailView):
    model = Problema
    context_object_name = 'matematica'
    template_name = 'Colegio/matematicaDetalle.html'

class MatematicaUpdate(LoginRequiredMixin, UpdateView):
    model = Problema
    form_class = ActualizacionProblema
    success_url = reverse_lazy('matematica')
    context_object_name = 'matematica'
    template_name = 'Colegio/matematicaEdicion.html'

class MatematicaDelete(LoginRequiredMixin, DeleteView):
    model = Problema
    success_url = reverse_lazy('matematica')
    context_object_name = 'matematica'
    template_name = 'Colegio/matematicaBorrado.html'




class FisicaLista(LoginRequiredMixin, ListView):
    context_object_name = 'fisicas'
    queryset = Problema.objects.filter(materia__startswith='fisica')
    template_name = 'Colegio/listafisica.html'

class FisicaDetalle(LoginRequiredMixin, DetailView):
    model = Problema
    context_object_name = 'fisica'
    template_name = 'Colegio/fisicaDetalle.html'

class FisicaUpdate(LoginRequiredMixin, UpdateView):
    model = Problema
    form_class = ActualizacionProblema
    success_url = reverse_lazy('fisica')
    context_object_name = 'fisica'
    template_name = 'Colegio/fisicaEdicion.html'

class FisicaDelete(LoginRequiredMixin, DeleteView):
    model = Problema
    success_url = reverse_lazy('fisica')
    context_object_name = 'fisica'
    template_name = 'Colegio/fisicaBorrado.html'


# CREACION PROBLEMA
class ProblemaCreacion(LoginRequiredMixin, CreateView):
    model = Problema
    form_class = FormularioNuevoProblema
    success_url = reverse_lazy('home')
    template_name = 'Colegio/ProblemaCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProblemaCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Colegio/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'Colegio/acercaDeMi.html', {})
