from django.urls import path
from ventas_app import views

urlpatterns = [
    path('Ventas',views.inicio_vistaVentas,name="Ventas"),
    path ("registrarVenta/",views.registrarVenta,name="registrarVenta"),
    path ("seleccionarVenta/<int:id_venta>",views.seleccionarVenta,name="seleccionarVenta"),
    path ("editarVenta/",views.editarVenta,name="editarVenta"),
    path ("borrarVenta/<int:id_venta>",views.borrarVenta, name="borrarVenta")
]