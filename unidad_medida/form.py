from django import forms
from .models import UnidadMedida

class UnidadMedidaForms(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = [
            "descripcion",
            "resumido",
            
        ]
        widgets = {
        "descripcion": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "resumido": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
       
       
    }