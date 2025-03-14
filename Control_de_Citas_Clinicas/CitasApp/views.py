from django.shortcuts import render, redirect, get_object_or_404
from .forms import CitaForm
from .models import Cita
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'CitasApp/signin.html', {'form': AuthenticationForm})
    
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'CitasApp/signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrecto.'})
        
        else:
            login(request, user)
            return redirect('inicio')
        

def crear_cuenta(request):

    if request.method == 'GET':
        return render(request, 'CitasApp/singup.html', {"form": UserCreationForm })
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio') #Toma el name de las urls que esta en el archivo urls.py
            except IntegrityError:
                return render(request, 'CitasApp/singup.html', {"form": UserCreationForm,"error": "El usuario ya existe."})
            
        return render(request, 'CitasApp/singup.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})
    

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('signin')

@login_required
def inicio(request):
    citas_form = CitaForm()
    lista_citas = Cita.objects.filter(estatus=True)

    context = {
        "citas": lista_citas,
        "citas_form": citas_form
    }

    return render(request, 'CitasApp/citas.html', context)

@login_required
def crear_cita(request):
    if request.method == 'POST':
        citas_form = CitaForm(request.POST)

        if citas_form.is_valid():
            try:
                citas_form.save()
                messages.success(request, 'Cita creada correctamente')
                return redirect('inicio')
            
            except Exception as e:
                messages.error(request, f'Error al crear la cita: {str(e)}')
                return render(request, 'CitasApp/citas.html', {'citas_form': citas_form})

        else:
            messages.error(request, 'Hubo un error en el formulario, revisa los datos.')
            return render(request, 'CitasApp/citas.html', {'citas_form': citas_form})

    else:
        citas_form = CitaForm()

    return render(request, 'CitasApp/citas.html', {'citas_form': citas_form})

@login_required
def  editar_eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'editar':
            editar_cita_form = CitaForm(request.POST, instance=cita)

            if editar_cita_form.is_valid():
                try:
                    editar_cita_form.save()
                    messages.info(request, 'Cita modificada correctamente.')
                    return redirect('inicio')
                
                except Exception as e:
                    return render(request, "CitasApp/detalle_cita.html", {"editar_cita_form": editar_cita_form, "error_message": f'Error al procesar el formulario. {e}'})
            else:
                messages.error('Algo salio mal al Modificar la cita.')
                return render(request, "CitasApp/detalle_cita.html", {"editar_cita_form": editar_cita_form, "error_message": "Hubo un error en el formulario, revisa los campos."})

        elif action == 'eliminar':
            cita.estatus = False
            cita.save()
            messages.info(request, 'Cita eliminada correctamente')
            return redirect('inicio')
    
    else:
        editar_cita_form = CitaForm(instance=cita)

    return render(request, 'CitasApp/detalle_cita.html', {'cita': cita, 'editar_cita_form': editar_cita_form})