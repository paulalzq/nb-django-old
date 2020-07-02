from django.db import models

# Create your models here.
class Servicio(models.Model):
    title = models.CharField(max_length=200, default='servicio')
    link = models.CharField(max_length=50, default='link_servicio')
    number = models.CharFiel(max_lenght=50, default='n+1')
    text = models.TextField()
    image = models.ImageField(upload_to='servicio', default='none')


    def __str__(self):
        return self.title

class Portafolio(models.Model):
    title = models.CharField(max_length=100, default='portafolio')
    link = models.CharField(max_length=50, default='link_solucion')
    description = models.TextField()
    image = models.ImageField(upload_to='portafolio', default='none')

    def __str__(self):
        return self.title
