"""tareaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionForm.views import formulario2, formulario3, formulario4, formulario5, home
from gestionForm import views
from gestionForm.class_view import ProjectList, ProjectCreate, ProjectUpdate, ProjectDelete, TrabajadorList, \
    TrabajadorCreate, TrabajadorUpdate, TrabajadorDelete
from gestionForm.class_view import ClienteCreate, ClienteDelete, ClienteUpdate, ClienteList
from gestionForm.class_view import MarcaCreate, MarcaDelete, MarcaUpdate, MarcaList
from gestionForm.class_view import ProductoCreate, ProductoDelete, ProductoUpdate, ProductoList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('project/index/', ProjectList.as_view(), name='project.index'),
    path('project/create/', ProjectCreate.as_view(), name='project.create'),
    path('project/edit/<int:pk>/', ProjectUpdate.as_view(), name='project.edit'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='project.delete'),

    # Seccion de Cliente

    path('cliente/index/', ClienteList.as_view(), name='cliente.index'),
    path('cliente/create/', ClienteCreate.as_view(), name='cliente.create'),
    path('cliente/edit/<int:pk>/', ClienteUpdate.as_view(), name='cliente.edit'),
    path('cliente/delete/<int:pk>/', ClienteDelete.as_view(), name='cliente.delete'),

    # Seccion de Marca

    path('marca/index/', MarcaList.as_view(), name='marca.index'),
    path('marca/create/', MarcaCreate.as_view(), name='marca.create'),
    path('marca/edit/<int:pk>/', MarcaUpdate.as_view(), name='marca.edit'),
    path('marca/delete/<int:pk>/', MarcaDelete.as_view(), name='marca.delete'),

    # Seccion de Producto

    path('producto/index/', ProductoList.as_view(), name='producto.index'),
    path('producto/create/', ProductoCreate.as_view(), name='producto.create'),
    path('producto/edit/<int:pk>/', ProductoUpdate.as_view(), name='producto.edit'),
    path('producto/delete/<int:pk>/', ProductoDelete.as_view(), name='producto.delete'),


    # Seccion de Trabajador

    path('trabajador/index/', TrabajadorList.as_view(), name='trabajador.index'),
    path('trabajador/create/', TrabajadorCreate.as_view(), name='trabajador.create'),
    path('trabajador/edit/<int:pk>/', TrabajadorUpdate.as_view(), name='trabajador.edit'),
    path('trabajador/delete/<int:pk>/', TrabajadorDelete.as_view(), name='trabajador.delete'),


    path('form2/', formulario2),
    path('form3/', formulario3),
    path('form4/', formulario4),
    path('form5/', formulario5),
]
