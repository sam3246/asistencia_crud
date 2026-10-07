from django.db import models

class asistencia(models.Model):
    tipo_documento = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    fecha = models.DateField()
    asistencia = models.BooleanField()
    
    def __str__(self):
        return self.nombres