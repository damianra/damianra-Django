from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Cursos, RedesSociales, Proyecto, Menu, Contacto, Categoria
from blog.forms import ContactoForm
from datetime import datetime


# Create your views here.

def index(request):
    cursos = Cursos.objects.order_by('id')
    redes = RedesSociales.objects.all()
    proyectos =  Proyecto.objects.all().order_by('-fecha').filter(estado='Publicado')[:5]
    menu = Menu.objects.order_by('id')

    contenido = {'cursos': cursos, 'Github': redes[0].link, 'Linkedin': redes[1].link, 'proyectos': proyectos, 'menu': menu}
    return render(request, 'blog/index.html', contenido)

def proyectos(request):
    redes = RedesSociales.objects.all()
    proyectos =  Proyecto.objects.all().order_by('-fecha').filter(estado='Publicado')
    menu = Menu.objects.order_by('id')

    contenido = {'proyectos': proyectos, 'Github': redes[0].link, 'Linkedin': redes[1].link, 'menu': menu}
    return render(request, 'blog/proyectos_index.html', contenido)

def proyecto (request, url):
    redes = RedesSociales.objects.all()
    proyectos =  Proyecto.objects.filter(url=url).first()
    menu = Menu.objects.order_by('id')

    contenido = {'proyecto': proyectos, 'Github': redes[0].link, 'Linkedin': redes[1].link, 'menu': menu}

    return render(request, 'blog/publicacion.html', contenido)


def categorias(request):
    cate = Categoria.objects.all()
    menu = Menu.objects.order_by('id')
    redes = RedesSociales.objects.all()

    contenido = {'categorias': cate, 'Github': redes[0].link, 'Linkedin': redes[1].link, 'menu': menu}

    return render(request, 'blog/categorias.html', contenido)


def contacto (request):
    redes = RedesSociales.objects.all()
    menu = Menu.objects.order_by('id')
    if request.method == 'POST':
        form = ContactoForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            fecha = datetime.now()

            nuevo_mensaje = Contacto(nombre=nombre, email=email, mensaje=mensaje, fecha=fecha)
            nuevo_mensaje.save()

            return redirect('inicio')
    else:
        form = ContactoForm()
    return render(request, 'blog/formulario.html', {'form': form, 'Github': redes[0].link, 'Linkedin': redes[1].link, 'menu': menu})