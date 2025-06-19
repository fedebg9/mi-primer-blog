from django.conf import settings
from django.db import models
from django.utils import timezone



class Publicacion(models.Model):

    entrenador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=200)
    jugadores = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):

        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.equipo

    
class Equipos(models.Model):
         
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    jugadores = models.TextField()
    partidos_ganados_en_la_temporada = models.IntegerField()
    partidos_perdidos_en_la_temporada = models.IntegerField(default=0)
    datos = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    def publicar(self):

        self.fecha_publicacion = timezone.now()
        self.save()
    def __str__(self):
        return self.equipo