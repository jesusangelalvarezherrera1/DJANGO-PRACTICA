from django.contrib import admin
from django.urls import path
from appalumnos.views import saludo, miEdad, index, alumnos, busqueda_alumnos, buscar_alumnos, busqueda_materias, buscar_materias, materias, docentes, busqueda_docentes, buscar_docentes, save_alumno, save_materia, save_docente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('edad/<int:edad>/', miEdad),
    path('', index),
    path('frmalumnos', alumnos),
    path('alumnos', save_alumno),
    path('frmmaterias', materias),
    path('materias', save_materia),
    path('frmdocentes', docentes),
    path('docentes', save_docente),
    path('frmbusqueda_alumnos', busqueda_alumnos),
    path('buscar_alumnos', buscar_alumnos),
    path('frmbusqueda_materias', busqueda_materias),
    path('buscar_materias', buscar_materias),
    path('frmbusqueda_docentes', busqueda_docentes),
    path('buscar_docentes', buscar_docentes),
    
    
]
