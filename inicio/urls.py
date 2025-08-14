from django.urls import path
from inicio.views import inicio, crear_auto, listado_de_autos, auto_detalle, AutoBorrar, AutoActualizar

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('autos/crear/<marca>/<modelo>/', crear_auto),
    path('autos/', listado_de_autos, name='listado_de_autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    path('autos/<int:id_auto>/', auto_detalle, name='auto_detalle'),
    path('autos/<int:pk>/borrar/', AutoBorrar.as_view(), name='auto_borrar'),
    path('autos/<int:pk>/actualizar/', AutoActualizar.as_view(), name='auto_actualizar'),
]
