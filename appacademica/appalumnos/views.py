from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import alumno
from .models import materia
from .models import docente
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def saludo(request):
    return  HttpResponse("Hola desde django")

def miEdad(request, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)

def index(request):
    return render(request, 'index.html')

def alumnos(request):
    return render(request, 'alumnos.html')


@csrf_exempt
def save_alumno(resquest):
    datos = json.loads(resquest.body)
    accion = datos.get("accion")
    idA = datos.get("idAlumno")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    dir = datos.get("direccion")
    tel = datos.get("telefono")
    if accion=="nuevo":
        editAlumno = alumno.objects.create(codigo=cod, nombre=nom, direccion=dir, telefono=tel)
    elif accion=="modificar":
        editAlumno = alumno.objects.get(id=idA)    
        editAlumno.codigo = cod
        editAlumno.nombre = nom
        editAlumno.direccion = dir
        editAlumno.telefono = tel
        editAlumno.save()

    elif accion=="eliminar":
        editAlumno = alumno.objects.get(id.idA)   
        editAlumno.delete() 
        
    return JsonResponse({'msg':'ok', 'idAlumno':editAlumno.id}, safe=False)     

def busqueda_alumnos(resquest):
    return render(resquest, 'busqueda_alumnos.html')

@csrf_exempt
def buscar_alumnos(resquest):
    data = json.loads(resquest.body)
    datos = alumno.objects.filter(nombre__icontains=data.get('buscar')).values('id', 'codigo', 'nombre', 'direccion', 'telefono')

    return JsonResponse(list(datos), safe=False)

def materias(request):
    return render(request, 'materias.html')

@csrf_exempt
def save_materia(resquest):
    datos = json.loads(resquest.body)
    accion = datos.get("accion")
    idM = datos.get("idMateria")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    u = datos.get("uv")
    if accion=="nuevo":
        editMateria = materia.objects.create(codigo=cod, nombre=nom, uv=u, )
    elif accion=="modificar":
        editMateria = materia.objects.get(id=idM)    
        editMateria.codigo = cod
        editMateria.nombre = nom
        editMateria.uv = u
        editMateria.save()
    elif accion=="eliminar":
        editMateria = materia.objects.get(id.idM)   
        editMateria.delete
    return JsonResponse({'msg':'ok', 'idMateria':editMateria.id}, safe=False)     


def busqueda_materias(request):
    return render(request, 'busqueda_materias.html')

@csrf_exempt
def buscar_materias(resquest):
    datos = materia.objects.values('id', 'codigo', 'nombre', 'uv')
    return JsonResponse(list(datos), safe=False)


def docentes(request):
    return render(request, 'docentes.html')

@csrf_exempt
def save_docente(resquest):
    datos = json.loads(resquest.body)
    accion = datos.get("accion")
    idD = datos.get("idDocente")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    dir = datos.get("direccion")
    tel = datos.get("telefono")
    if accion=="nuevo":
        editDocente = docente.objects.create(codigo=cod, nombre=nom, direccion=dir, telefono=tel)
    elif accion=="modificar":
        editDocente = docente.objects.get(id=idD)    
        editDocente.codigo = cod
        editDocente.nombre = nom
        editDocente.direccion = dir
        editDocente.telefono = tel
        editDocente.save()
    elif accion=="eliminar":
        editDocente = docente.objects.get(id.idD)   
        editDocente.delete
    return JsonResponse({'msg':'ok', 'idDocente':editDocente.id}, safe=False)     


def busqueda_docentes(request):
    return render(request, 'busqueda_docentes.html')

@csrf_exempt
def buscar_docentes(resquest):
    datos = docente.objects.values('id', 'codigo', 'nombre', 'direccion', 'telefono')
    return JsonResponse(list(datos), safe=False)
