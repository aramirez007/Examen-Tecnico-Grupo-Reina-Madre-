from django.db import models

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    paciente = models.TextField()
    tipo = models.CharField(max_length=20, choices=[
        ('1', 'Consulta'),
        ('2', 'Servicio'),
        ('3', 'Tratamiento'),
        ('4', 'Otro')
    ])
    medico = models.TextField()
    numerocita = models.IntegerField()
    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'cita'
        verbose_name_plural = 'citas'

    def __str__(self):
        return f'Cita para {self.paciente} el día {self.fecha} con el Medico {self.medico}'