from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='signin'),
    path('singup/', views.crear_cuenta, name='singup'),
    path('logout/', views.cerrar_sesion, name='singout'),

    path('citas/', views.inicio, name='inicio'),
    path('crear-cita/', views.crear_cita, name='crear_cita'),
    path('editar-eliminar-cita/<int:cita_id>/', views.editar_eliminar_cita, name='editar_eliminar_cita'),

]