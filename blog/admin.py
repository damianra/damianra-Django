from django.contrib import admin
from blog.models import Cursos, RedesSociales, Proyecto, Categoria, Tag, Menu, Contacto

def publicar(modeladmin, request, queryset):
    queryset.update(estado='Publicado')

class ContactoDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fecha']
    list_filter = ('nombre',)

class MenuDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'link']
    list_filter = ('nombre',)

class SocialMedia(admin.ModelAdmin):
    list_display = ['nombre', 'link']
    list_filter = ('nombre',)

class CursosDisplay(admin.ModelAdmin):
    list_display = ['titulo']
    list_filter = ('titulo',)

class ProyectoDisplay(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'categoria', 'estado']
    list_filter = ('titulo', 'fecha')
    ordering = ['-fecha']
    actions = [publicar]


class CategoriaDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    list_filter = ('nombre',)

class TagDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    list_filter = ('nombre',)

# Register your models here.
admin.site.register(Cursos, CursosDisplay)
admin.site.register(RedesSociales, SocialMedia)
admin.site.register(Proyecto, ProyectoDisplay)
admin.site.register(Categoria, CategoriaDisplay)
admin.site.register(Tag, TagDisplay)
admin.site.register(Menu, MenuDisplay)
admin.site.register(Contacto, ContactoDisplay)
