from django import forms
from .models import Cita
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                pass
        return value
    

class CitaForm(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'paciente', 'tipo', 'medico', 'numerocita']
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del paciente'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del medico'}),
            'numerocita': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')

        if instance and instance.pk: #Si ya existe el registro se deshabilitaran los apartados
            self.fields['paciente'].widget.attrs['readonly'] = 'readonly'
            self.fields['numerocita'].widget.attrs['readonly'] = 'readonly'

        else:
            self.fields['paciente'].widget.attrs['readonly'] = False
            self.fields['numerocita'].widget.attrs['readonly'] = False

        if instance and instance.fecha:
            self.initial['fecha'] = instance.fecha.strftime('%Y-%m-%d')