from django.urls import path
from .views import Recibidos

app_name = 'mensaje'

urlpatterns = [
    path('recibidos/',   Recibidos ,name='Recibidos' )
]