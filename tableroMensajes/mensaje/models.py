from django.db import models
from django.utils import timezone


# Create your models here.
#punto 2
class Mensaje (models.Model):
    textoDelMensaje = models.TextField()
    remitente = models.CharField(max_length = 200)
    destinatario = models.CharField(max_length = 200)
    fechayHora = models.DateTimeField(default = timezone.now)




