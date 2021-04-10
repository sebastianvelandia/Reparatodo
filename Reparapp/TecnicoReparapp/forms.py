from django import forms
from .models import Taller,CallCenter

class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ('Taller_id', 'Nombre_taller')

class CallCenterForm(forms.ModelForm):
    class Meta:
        model = CallCenter
        fields = ('CallCenter_NIT', 'Nombre_callcenter','Direccion')
