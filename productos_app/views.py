from django.shortcuts import render,redirect
from .models import Producto
# Create your views here.
def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request,'gestionarProducto.html',{"misproductos":losproductos})

def registrarProducto(request):
    id_producto=request.POST["numid_producto"]
    nombre=request.POST["txtnombre"]
    tamaño=request.POST["txttamaño"]
    precio=request.POST["numprecio"]
    calidad=request.POST["txtcalidad"]
    cantidad=request.POST["numcantidad"]
    peso=request.POST["numpeso"]


    guardarproducto=Producto.objects.create(
        id_producto=id_producto,nombre=nombre,tamaño=tamaño,precio=precio,calidad=calidad,cantidad=cantidad,peso=peso
    ) # GUARDAR EL REGISTRO

    return redirect("Producto")

def seleccionarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misproductos": producto})

def editarProducto(request):
    id_producto=request.POST["numid_producto"]
    nombre=request.POST["txtnombre"]
    tamaño=request.POST["txttamaño"]
    precio=request.POST["numprecio"]
    calidad=request.POST["txtcalidad"]
    cantidad=request.POST["numcantidad"]
    peso=request.POST["numpeso"]
    producto = Producto.objects.get(id_producto=id_producto)
    producto.nombre=nombre
    producto.tamaño=tamaño
    producto.precio=precio
    producto.calidad=calidad
    producto.cantidad=cantidad
    producto.peso=peso
    producto.save() # GUARDAR EL REGISTRO ACTUALIZADO
    return redirect("Producto")

def borrarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete() # BORRAR EL REGISTRO
    return redirect("Producto")
