from django.db import models

class persona(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellidos = models.CharField(max_length=100, blank=False)
    foto = models.ImageField(upload_to='foto/',blank=True)
    archivo = models.FileField(upload_to='archivo/' ,blank=True)
    def __unicode__(self):
        return self.nombre


