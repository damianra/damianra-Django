
from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='inicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyectos/<url>/', views.proyecto, name='proyecto'),
    path('contacto/', views.contacto, name='contacto')
]
