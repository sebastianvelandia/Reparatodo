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
<<<<<<< HEAD
        fields = ('factura_id', 'costo_orden','orden','agente','callCenter','fecha_retiro')
=======
        fields = ('factura_id', 'costo_orden','orden','tecnicoEspecialista','callCenter','fecha_retiro')
>>>>>>> parent of c9a8782... login
