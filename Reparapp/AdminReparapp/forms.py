from django import forms
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Agente, TecnicoEspecialista, Usuario
from TecnicoReparapp.models import Taller


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class AgenteForm(forms.ModelForm):
    agente_id = forms.CharField(label='Cédula', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la cédula',
            'id': 'password2',
            'required': 'required'
        }
    ))
    class Meta:
        model = Usuario
        fields = ('nombres','apellidos','email','telefono')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('agente_id')
        user.set_password(self.cleaned_data.get('agente_id'))
        user.usuario_agente = True
        user.save()
        agente = Agente.objects.create(user=user)
        agente.agente_id = self.cleaned_data.get('agente_id')
        agente.save()
        return user


# class AgenteForm(UserCreationForm):
#     username = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     nombres = forms.CharField(required=True)
#     apellidos = forms.CharField(required=True)
#     agente_id = forms.CharField(required=True)
#     telefono = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = Usuario

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.username = self.cleaned_data.get('agente_id')
#         user.email = self.cleaned_data.get('email')
#         user.nombres = self.cleaned_data.get('nombres')
#         user.apellidos = self.cleaned_data.get('apellidos')
#         user.telefono = self.cleaned_data.get('telefono')
#         user.usuario_agente = True
#         user.save()
#         agente = Agente.objects.create(user=user)
#         agente.agente_id = self.cleaned_data.get('agente_id')
#         agente.save()
#         return user


class TecnicoEspecialistaForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    nombres = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
    tecnico_id = forms.CharField(required=True)
    telefono = forms.CharField(required=True)
    taller = forms.ModelChoiceField(queryset=Taller.objects.all())

    class Meta(UserCreationForm.Meta):
        model = Usuario

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.nombres = self.cleaned_data.get('nombres')
        user.apellidos = self.cleaned_data.get('apellidos')
        user.telefono = self.cleaned_data.get('telefono')
        user.usuario_tecnico = True
        user.save()
        tecnico = TecnicoEspecialista.objects.create(user=user)
        tecnico.agente_id = self.cleaned_data.get('agente_id')
        tecnico.taller = self.cleaned_data.get('taller')
        agente.save()
        return user

# class AgenteForm(forms.ModelForm):
#    pass
#     class Meta:
#         model = Agente
#         fields = ('username', 'email','nombres','apellidos','password','agente_id','telefono','usuario_agente')

# class TecnicoEspecialistaForm(forms.ModelForm):
#    pass
#     class Meta:
#         model = TecnicoEspecialista
#         fields = ('username', 'nombres','apellidos','password','tecnico_id','telefono','taller','usuario_tecnico')
