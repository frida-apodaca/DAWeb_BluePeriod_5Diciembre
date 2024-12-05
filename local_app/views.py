from django.shortcuts import render,redirect
from .models import Local
# Create your views here.
def inicio_vistaLocal(request):
    loslocales=Local.objects.all()
    return render(request,'gestionarLocal.html',{"mislocales":loslocales})

def registrarLocal(request):
    id_local=request.POST["numid_local"]
    nombre=request.POST["txtnombre"]
    capacidad=request.POST["numcapacidad"]
    empleados=request.POST["txtempleado"]
    dueño=request.POST["txtdueño"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]


    guardarlocal=Local.objects.create(
        id_Local=id_local,nombre=nombre,capacidad=capacidad,empleados=empleados,dueño=dueño,direccion=direccion,telefono=telefono
    ) # GUARDAR EL REGISTRO

    return redirect("Local")

def seleccionarLocal(request,id_local):
    local=Local.objects.get(id_Local=id_local)
    return render(request, "editarLocal.html", {"mislocales": local})

def editarLocal(request):
    id_local=request.POST["numid_local"]
    nombre=request.POST["txtnombre"]
    capacidad=request.POST["numcapacidad"]
    empleado=request.POST["txtempleado"]
    dueño=request.POST["txtdueño"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    local = Local.objects.get(id_Local=id_local)
    local.nombre=nombre
    local.capacidad=capacidad
    local.empleados=empleado
    local.dueño=dueño
    local.direccion=direccion
    local.telefono=telefono
    local.save() # GUARDAR EL REGISTRO ACTUALIZADO
    return redirect("Local")

def borrarLocal(request,id_local):
    local=Local.objects.get(id_Local=id_local)
    local.delete() # BORRAR EL REGISTRO
    return redirect("Local")
