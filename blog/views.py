from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from django.contrib.auth.models import User
from .models import Equipos


def lista_public(request):
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    usr_id = request.GET.get('usuario')
    if usr_id:
        publicaciones= publicaciones.filter(entrenador__id=usr_id)
    
    usuarios=User.objects.all()
    if usr_id:
        usuario_activo = int(usr_id)
    else:
        usuario_activo = None
    
    return render(request, 'blog/lista_public.html', {
        'publicaciones': publicaciones,
        'usuarios': usuarios,
        'usuario_activo': usuario_activo,
    }) 

def equipos_lista(request):
    equipos = Equipos.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    usr_id = request.GET.get('usuario')
    if usr_id:
        equipos = equipos.filter(autor__id=usr_id)
    
    usuarios = User.objects.all()
    if usr_id:
        usuario_activo = int(usr_id)
    else:
        usuario_activo = None

    return render(request, 'blog/equipos_lista.html', {
        'equi': equipos,
        'usuarios': usuarios,
        'usuario_activo': usuario_activo,
    })