from django.urls import path
from .views import *


app_name = "empleados_app"

urlpatterns = [
    path('listar_empleados/', ListarEmpleados.as_view()),
    path('listar_area/<name>', ListarPorArea.as_view()),
    path('buscar_empleado/', ListarEmpleadosPorPalabraClave.as_view()),
    path('listar_habilidades/<int:id>', ListarHabilidadesEmpleado.as_view()),
    path('detalle_empleado/<pk>', EmpleadoDetailView.as_view()),
    path('crear_empleado/', EmpleadoCreateView.as_view()),
    path('success/', SuccessView.as_view(), name="correcto"),
    path('actualizar_empleado/<pk>', EmpleadoUpdateView.as_view(), name="modificar_empleado"),
    path('eliminar_empleado/<pk>', EmpleadoDeleteView.as_view(), name="eliminar_empleado")
]
