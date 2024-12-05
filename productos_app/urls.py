from django.urls import path
from productos_app import views

urlpatterns = [
    path('Producto',views.inicio_vistaProducto,name="Producto"),
    path ("registrarProducto/",views.registrarProducto,name="registrarEmpleado"),
    path ("seleccionarProducto/<int:id_producto>",views.seleccionarProducto,name="seleccionarProducto"),
    path ("editarProducto/",views.editarProducto,name="editarProducto"),
    path ("borrarProducto/<int:id_producto>",views.borrarProducto, name="borrarProducto")
]