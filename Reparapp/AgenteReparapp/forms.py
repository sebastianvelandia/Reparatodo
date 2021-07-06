from django import forms
from django.core.checks import messages
from django.db import transaction
from .models import Cliente, Producto, Orden, Factura
from AdminReparapp.models import Agente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cliente_id','nombre', 'telefono')


class NuevaOrdenClienteForm(forms.ModelForm):
    cliente_id = forms.CharField(label='Cédula del cliente', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la cédula',
            'id': 'cliente_id',
            'required': 'required'
        }
    ))

    nombre_cliente = forms.CharField(label='Nombre del cliente', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del cliente',
            'id': 'nombre_cliente',
            'required': 'required'
        }
    ))
    telefono_cliente = forms.CharField(label='Teléfono del cliente', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Teléfono del cliente',
            'id': 'telefono_cliente',
            'required': 'required'
        }
    ))

    averia_producto = forms.CharField(label='Averia', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la averia',
            'id': 'averia_producto',
            'required': 'required'
        }
    ))

    electrodomestico = forms.CharField(label='Nombre del electrodoméstico', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el electrodoméstico',
            'id': 'electrodomestico',
            'required': 'required'
        }
    ))

    observaciones = forms.CharField(label='Observaciones', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese observaciones',
            'id': 'observaciones',
            'required': 'required'
        }
    ))

    agente_id = forms.IntegerField(label='Ingrese id del agente :', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese id agente',
            'id': 'agente_id',
            'required': 'required'
        }
    ))

    class Meta:
        model = Orden
        fields = ('estado',)

    @transaction.atomic
    def save(self):
        orden = super().save(commit=False)
        producto = Producto.objects.create()
        producto.averia = self.cleaned_data.get('averia_producto')
        producto.nombre_electrodomestico = self.cleaned_data.get(
            'electrodomestico')
        producto.save()
 
        cliente = Cliente.objects.create()
        cliente.nombre = self.cleaned_data.get('nombre_cliente')
        cliente.cliente_id = self.cleaned_data.get('cliente_id')
        cliente.telefono = self.cleaned_data.get('telefono_cliente')
        cliente.save()

        query = Agente.objects.filter( agente_id=self.cleaned_data.get('agente_id'))
        agente = query[0]
        orden = Orden.objects.create( agente=agente, cliente=cliente, producto=producto)
        orden.observaciones = self.cleaned_data.get('observaciones')
        query = Cliente.objects.filter(cliente_id='')
        if query:
            cliente = query[0]
            cliente.delete()
        return orden

class NuevaOrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('estado','observaciones')
    cliente_identificacion = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)

    averia_producto = forms.CharField(label='Averia', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la averia',
            'id': 'averia_producto',
            'required': 'required'
        }
    ))

    electrodomestico = forms.CharField(label='Nombre del electrodoméstico', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el electrodoméstico',
            'id': 'electrodomestico',
            'required': 'required'
        }
    ))

    # observaciones_orden = forms.CharField(label='Observaciones', widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Ingrese observaciones',
    #         'id': 'observaciones_orden',
    #         'required': 'required'
    #     }
    # ))

    agente_id = forms.CharField(label='Ingrese id del agente :', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese id agente',
            'id': 'agente_id',
            'required': 'required'
        }
    ))

    @transaction.atomic
    def save(self):
        orden = super().save(commit=False)
        producto = Producto.objects.create()
        producto.averia = self.cleaned_data.get('averia_producto')
        producto.nombre_electrodomestico = self.cleaned_data.get('electrodomestico')
        producto.save()

        query1 = Cliente.objects.filter(cliente_id = self.cleaned_data.get('cliente_identificacion'))
        cliente = query1[0]
        query2 = Agente.objects.filter( agente_id=self.cleaned_data.get('agente_id'))
        if query2:
            agente = query2[0]
        else:
            raise("No se encontró al agente")
        orden = Orden.objects.create( agente=agente, cliente=cliente, producto=producto)
        #orden.observaciones = self.cleaned_data.get('observaciones_orden')
        query = Cliente.objects.filter(cliente_id='')
        if query:
            cliente = query[0]
            cliente.delete()
        return orden
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo_id', 'averia', 'nombre_electrodomestico')


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('estado','cliente','producto', 'observaciones')


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura

        fields = ('factura_id', 'costo_orden', 'orden',
                  'agente', 'callCenter', 'fecha_retiro')

