from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import ProjectForm, ProductoForm, TrabajadorForm
from .models import Project, Producto, Trabajador
from .forms import ClienteForm
from .models import Cliente
from .forms import MarcaForm
from .models import Marca


class ProjectList(ListView):
    model = Project
    template_name = 'project/index.html'


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project.index')


class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project.index')


class ProjectDelete(DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'
    success_url = reverse_lazy('project.index')


# Seccion de Cliente
class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/index.html'


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('cliente.index')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('cliente.index')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente.index')


# Seccion de Marca
class MarcaList(ListView):
    model = Marca
    template_name = 'marca/index.html'


class MarcaCreate(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/create.html'
    success_url = reverse_lazy('marca.index')


class MarcaUpdate(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/create.html'
    success_url = reverse_lazy('marca.index')


class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'marca/cliente_confirm_delete.html'
    success_url = reverse_lazy('marca.index')


# Seccion de Producto
class ProductoList(ListView):
    model = Producto
    template_name = 'producto/index.html'


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/create.html'
    success_url = reverse_lazy('producto.index')


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/create.html'
    success_url = reverse_lazy('producto.index')


class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html'
    success_url = reverse_lazy('producto.index')


# Seccion de Trabajador
class TrabajadorList(ListView):
    model = Trabajador
    template_name = 'trabajador/index.html'


class TrabajadorCreate(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('trabajador.index')


class TrabajadorUpdate(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('trabajador.index')


class TrabajadorDelete(DeleteView):
    model = Trabajador
    template_name = 'trabajador/trabajador_confirm_delete.html'
    success_url = reverse_lazy('trabajador.index')
