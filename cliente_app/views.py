from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.
def inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarCliente.html',{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST["numid_cliente"]
    nombre=request.POST["txtnombre"]
    sexo=request.POST["txtsexo"]
    productos=request.POST["txtproductos"]
    historial=request.POST["txthistorial"]
    metodo_pago=request.POST["txtmetodo_pago"]
    telefono=request.POST["numtelefono"]


    guardarcliente=Cliente.objects.create(
        id_cliente=id_cliente,nombre=nombre,sexo=sexo,productos=productos,historial=historial,metodo_pago=metodo_pago,telefono=telefono
    ) # GUARDAR EL REGISTRO

    return redirect("Clientes")

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"misclientes": cliente})

def editarCliente(request):
    id_cliente=request.POST["numid_cliente"]
    nombre=request.POST["txtnombre"]
    sexo=request.POST["txtsexo"]
    productos=request.POST["txtproductos"]
    historial=request.POST["txthistorial"]
    metodo_pago=request.POST["txtmetodo_pago"]
    telefono=request.POST["numtelefono"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.sexo=sexo
    cliente.productos=productos
    cliente.historial=historial
    cliente.metodo_pago=metodo_pago
    cliente.telefono=telefono
    cliente.save() # GUARDAR EL REGISTRO ACTUALIZADO
    return redirect("Clientes")

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete() # BORRAR EL REGISTRO
    return redirect("Clientes")
