from django import forms
from .models import Estructura

class EstructuraForm(forms.ModelForm):
    class Meta:
        model = Estructura
        fields = ['clase', 'marca', 'modelo', 'parte', 'elemento', 'nro_pieza', 'precio']

class BusquedaForm(forms.Form):
    q =forms.CharField( label="Buscar", required=False, help_text= "cod. modelo, nro pieza, parte, elemento, etc")