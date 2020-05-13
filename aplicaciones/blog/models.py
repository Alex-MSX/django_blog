from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    #auto_now: se actualiza cada vez que se edita el modelo
    #auto_now_add: se añade solamente al momento de la creación del objecto

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido = models.CharField(max_length=200, null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, null=False, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo
