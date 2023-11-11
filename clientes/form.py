from django import forms
from .models import Clientes

class ClientesForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            "nombre",
            "apellido",
            "documento",
            "direccion",
            "telefono",
            "correo",
        ]
        widgets = {
        "nombre": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "apellido": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "documento": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "direccion": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "telefono": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
        "correo": forms.TextInput(attrs={"class": "form-control my-small-input", "type": "text"}),
       
    }
