from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.html import format_html

# Create your models here.
class Cursos(models.Model):
    titulo = models.CharField(max_length=250)
    finalizado = models.CharField(max_length=250)
    link = models.CharField(max_length=250, null=True)
    id_credencial = models.CharField(max_length=250, null=True)

    def __str__(self):
        return '%s' % self.titulo

class RedesSociales(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.nombre

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return '%s' % self.nombre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre.lower().replace(' ', '-'))
        super(Categoria, self).save(*args, **kwargs)
        
    

class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return '%s' % self.nombre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre.lower().replace(' ', '-'))
        super(Tag, self).save(*args, **kwargs)

class Proyecto(models.Model):
    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    ESTADO = (
        (Borrador,'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )
        

    titulo = models.CharField(max_length=250)
    url = models.CharField(max_length=250, blank=True, unique=True, null=True)
    contenido = RichTextUploadingField()
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    imagenDestacada = models.FileField(upload_to='imgproyectos', blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO, default='Borrador')
    descripcion_corta = models.CharField(max_length=100, blank=True, null=True, default='Descripcion Corta')


    def __str__(self):
        return '%s' % self.titulo

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo.lower().replace(' ', '-'))
        super(Proyecto, self).save(*args, **kwargs)
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mensaje = RichTextField()
    fecha = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre

