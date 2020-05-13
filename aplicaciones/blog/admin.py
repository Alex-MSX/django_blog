from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#Para agregar los botones de importar/exportar hay que hacer un pip install django-import-export y crear la clase model_resource y añadirlo a la clase de model_admin
class Categoria_Resource(resources.ModelResource):
    class Meta:
        model = models.Categoria

class Categoria_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_actualizacion','fecha_creacion')
    resource_class = Categoria_Resource

class Autor_Resource(resources.ModelResource):
    class Meta:
        model = models.Autor

class Autor_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre','apellido','correo']
    list_display = ('nombre','apellido','correo','estado','fecha_creacion')
    resource_class = Autor_Resource

admin.site.register(models.Autor, Autor_Admin)
admin.site.register(models.Categoria, Categoria_Admin)
admin.site.register(models.Publicacion)
