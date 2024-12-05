from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,'gestionarEmpleado.html',{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["numcodigo"]
    nombre=request.POST["txtnombre"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    sueldo=request.POST["numsueldo"]
    sexo=request.POST["txtsexo"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]


    Empleado.objects.create(
        id_empleado=id_empleado,nombre=nombre,fecha_nacimiento=fecha_nacimiento,sueldo=sueldo,sexo=sexo,telefono=telefono,direccion=direccion,fecha_ingreso=fecha_ingreso
    ) # GUARDAR EL REGISTRO

    return redirect("Empleados")

def seleccionarEmpleado(request,codigo):
    empleado=Empleado.objects.get(id_empleado=codigo)
    fecha_nacimiento=empleado.fecha_nacimiento.strftime('%Y-%m-%d')
    return render(request, "editarEmpleado.html", {"Empleado": empleado, "Empleado": empleado, "fecha_nacimiento" : fecha_nacimiento})

def editarEmpleado(request):
    id_empleado=request.POST["numcodigo"]
    nombre=request.POST["txtnombre"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    sueldo=request.POST["numsueldo"]
    sexo=request.POST["txtsexo"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.fecha_nacimiento=fecha_nacimiento
    empleado.sueldo=sueldo
    empleado.sexo=sexo
    empleado.telefono=telefono
    empleado.direccion=direccion
    empleado.fecha_ingreso=fecha_ingreso
    empleado.save() # GUARDAR EL REGISTRO ACTUALIZADO
    return redirect("Empleados")

def borrarEmpleado(request,codigo):
    empleado=Empleado.objects.get(id_empleado=codigo)
    empleado.delete() # BORRAR EL REGISTRO
    return redirect("Empleados")
