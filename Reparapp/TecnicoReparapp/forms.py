from django import forms
from .models import Taller,CallCenter

class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ('taller_id', 'nombre_taller')

class CallCenterForm(forms.ModelForm):
    class Meta:
        model = CallCenter
        fields = ('callCenter_NIT', 'nombre_callcenter','direccion')
