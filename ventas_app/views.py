from django.shortcuts import render,redirect
from .models import Ventas
# Create your views here.
def inicio_vistaVentas(request):
    lasventas=Ventas.objects.all()
    return render(request,'gestionarVenta.html',{"misventas":lasventas})

def registrarVenta(request):
    id_venta=request.POST["numid_venta"]
    id_empleado=request.POST["numid_empleado"]
    id_cliente=request.POST["numid_cliente"]
    fecha_venta=request.POST["txtfecha_venta"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]


    guardarVentas=Ventas.objects.create(
        id_venta=id_venta,id_empleado=id_empleado,id_cliente=id_cliente,fecha_venta=fecha_venta,cantidad=cantidad,total=total
    ) # GUARDAR EL REGISTRO

    return redirect("Ventas")

def seleccionarVenta(request,id_venta):
    venta=Ventas.objects.get(id_venta=id_venta)
    return render(request, "editarVenta.html", {"misventas": venta})

def editarVenta(request):
    id_venta=request.POST["numid_venta"]
    id_empleado=request.POST["numid_empleado"]
    id_cliente=request.POST["numid_cliente"]
    fecha_venta=request.POST["txtfecha_venta"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]
    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_empleado=id_empleado
    venta.id_cliente=id_cliente
    venta.fecha_venta=fecha_venta
    venta.cantidad=cantidad
    venta.total=total
    venta.save() # GUARDAR EL REGISTRO ACTUALIZADO
    return redirect("Ventas")

def borrarVenta(request,id_venta):
    venta=Ventas.objects.get(id_venta=id_venta)
    venta.delete() # BORRAR EL REGISTRO
    return redirect("Ventas")
