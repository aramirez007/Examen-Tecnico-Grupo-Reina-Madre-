from django.urls import path
from . import views

urlpatterns = [
    path('', views.citas_eliminadas, name='citas_eliminadas'),
    path('cita-eliminada-detalle/<int:cita_id>/', views.citas_eliminadas_detalle, name='citas_eliminadas_detalle'),

]