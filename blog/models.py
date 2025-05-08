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