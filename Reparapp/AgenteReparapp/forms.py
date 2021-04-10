from django import forms
from .models import Cliente,Producto,Orden,Factura

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cliente_id', 'nombre','telefono')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo_id', 'averia','nombre_electrodomestico')

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('orden_id', 'observaciones','estado',
        'agente','cliente','tecnico_epecialista','producto')

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('factura_id', 'costo_orden','orden','tecnicoEspecialista','callCenter','fecha_retiro')