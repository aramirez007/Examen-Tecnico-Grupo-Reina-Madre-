from django.shortcuts import render, redirect, get_object_or_404
from CitasApp.models import Cita
from CitasApp.forms import CitaForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def citas_eliminadas(request):
    lista_citas_eliminadas = Cita.objects.filter(estatus=False)
    
    context = {
        'citas': lista_citas_eliminadas
    }
    return render(request, 'CitasAppEliminadas/citas_eliminadas.html', context)

@login_required
def citas_eliminadas_detalle(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    cita_eliminada_detalle = CitaForm(instance=cita)

    context = {
        'cita':cita,
        'cita_eliminada': cita_eliminada_detalle
    }

    return render(request, 'CitasAppEliminadas/citas_eliminadas_detalle.html', context)