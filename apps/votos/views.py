from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Voto, Charla
from .forms import RegistrarCharlaForm

class ListarEstadoView(ListView):
    context_object_name = 'charlas'
    queryset = Charla.posibles.all()
    template_name = 'index.html'


class ListarAgendadoView(ListarEstadoView):
    queryset = Charla.agendadas.all()


class ListarFinalizadoView(ListarEstadoView):
    queryset = Charla.finalizadas.all()


class RegistrarCharlaView(CreateView):
    form_class = RegistrarCharlaForm
    model = Charla
    success_url = reverse_lazy('index')
    template_name = 'registrar_charla.html'

    def get_form_kwargs(self):
        if self.request.method in ('POST', 'PUT'):
            self.object = self.model()
            self.object.usuario = self.request.user
        kwargs = super(RegistrarCharlaView, self).get_form_kwargs()
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RegistrarCharlaView, self).dispatch(*args, **kwargs)