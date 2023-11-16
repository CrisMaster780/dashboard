from django import forms
from .models import Impuestos

class ImpuestosForms(forms.ModelForm):
    class Meta:
        model = Impuestos
        fields = [
            "descripcion",
            "porcentaje",
            
        ]
        widgets = {
        "descripcion": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "porcentaje": forms.TextInput(attrs={"class": "form-control my-small-input", 'type': 'number'}),
       
       
    }