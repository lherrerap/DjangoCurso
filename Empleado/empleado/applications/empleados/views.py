from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Empleado
from django.views.generic import *
# Create your views here.

class ListarEmpleados(ListView):
    template_name = 'empleado/listar_empleados.html'
    paginate_by = 4
    model = Empleado
    context_object_name = 'lista_empleados'

class ListarPorArea(ListView):
    template_name = 'empleado/listar_por_area.html'
    model = Empleado
    queryset = Empleado.objects.filter(
        departamento__name='Area de Ingresos'
    )
    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista
    context_object_name = 'lista_empleados_area'
    
class ListarEmpleadosPorPalabraClave(ListView):
    template_name='empleado/listar_empleados_clave.html'
    context_object_name = 'lista_empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword"," ")
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListarHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.kwargs.get('id')
        empleado = Empleado.objects.get(id=id_empleado)
        return empleado.habilidad.all()
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detalle_empleado.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/crear_empleado.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidad',
    ]
    success_url = reverse_lazy('empleados_app:correcto')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = f"{empleado.first_name} {empleado.last_name}"
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class SuccessView(TemplateView):
    template_name = "empleado/vista_success.html"


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/actualizar_empleado.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidad',
    ]
    success_url = reverse_lazy('empleados_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/eliminar_empleado.html"
    success_url = reverse_lazy('empleados_app:correcto')
    




# 1. Listar todos los empleados de la empresa
# 2. Listar todos los empleados que pertenecen a un area de la empresa
# 3. Listar los empleados por trabajo
# 4. Listar los empleados por palabra clave
# 5. Listar habilidades de un empleado




