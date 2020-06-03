from django import forms
from .models import Project, Marca, Producto, Cliente, Trabajador


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"


class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = "__all__"
