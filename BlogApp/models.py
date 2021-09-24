from django.db import models

# Create your models here.
class Suscripto(models.Model):
    full_name=models.CharField(max_length=100, verbose_name="Nombre completo")
    email=models.EmailField(verbose_name="Correo")

class Suscripto2(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)

####
from django.contrib.auth.models import User
###
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    titulo=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    actualizado_el=models.DateTimeField(auto_now=True)
    contenido=models.TextField()

    creado_el=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering=['-creado_el']

    def __str__(self):
        return self.titulo


