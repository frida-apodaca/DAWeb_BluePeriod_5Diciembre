from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.
def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request,'gestionarProveedor.html',{"misproveedores":losproveedores})

def registrarProveedor(request):
    id_proveedor=request.POST["numid_proveedor"]
    nombre=request.POST["txtnombre"]
    productos=request.POST["txtproductos"]
    cantidad_productos=request.POST["numcantidad_productos"]
    direccion=request.POST["txtdireccion"]
    fecha_contratacion=request.POST["txtfecha_contratacion"]
    sueldo=request.POST["numsueldo"]


    guardarProveedor=Proveedor.objects.create(
        id_proveedor=id_proveedor,nombre=nombre,productos=productos,cantidad_productos=cantidad_productos,direccion=direccion,fecha_contratacion=fecha_contratacion,sueldo=sueldo
    ) # GUARDAR EL REGISTRO

    return redirect("Proveedor")

def seleccionarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedor.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id_proveedor=request.POST["numid_proveedor"]
    nombre=request.POST["txtnombre"]
    productos=request.POST["txtproductos"]
    cantidad_productos=request.POST["numcantidad_productos"]
    direccion=request.POST["txtdireccion"]
    fecha_contratacion=request.POST["txtfecha_contratacion"]
    sueldo=request.POST["numsueldo"]
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre=nombre
    proveedor.productos=productos
    proveedor.cantidad_productos=cantidad_productos
    proveedor.direccion=direccion
    proveedor.fecha_contratacion=fecha_contratacion
    proveedor.sueldo=sueldo
    proveedor.save() # GUARDAR EL REGISTRO ACTUALIZADO
    return redirect("Proveedor")

def borrarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete() # BORRAR EL REGISTRO
    return redirect("Proveedor")
