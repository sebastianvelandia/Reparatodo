from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Agente,TecnicoEspecialista
 
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'


class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = ('agente_id', 'nombre','telefono')

class TecnicoEspecialistaForm(forms.ModelForm):
    class Meta:
        model = TecnicoEspecialista
        fields = ('tecnico_id','nombre','telefono','taller')
  
