from django.shortcuts import render
from .models import Mensaje
# Create your views here.
def Recibidos(request):
    mensajesRecibidos = Mensaje.objects.all()

    return render(request, 'mensajes/recibido.html', {'mensajes' : mensajesRecibidos})

