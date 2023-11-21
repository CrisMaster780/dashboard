from django import forms
from .models import Productos, Clasificacion, Marca
from impuestos.models import Impuestos
from unidad_medida.models import UnidadMedida


class ProductosForms(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            "descripcion",
            "codigo_barra",
            "codigo_producto",
            "lote",
            "precio_costo",
            "precio_venta",
            "precio_mayorista",
            'existencia',
            "vencimiento",
            "marca",
            "clasificacion",
            "impuesto",
            "unidad_medida",
        ]
        widgets = {
            "descripcion": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "text"}
            ),
            "codigo_barra": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "text"}
            ),
            "codigo_producto": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "text"}
            ),
            "lote": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "text"}
            ),
            "precio_costo": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "number"}
            ),
            "precio_venta": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "number"}
            ),
            "precio_mayorista": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "number"}
            ),
             "existencia": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "number"}
            ),
            "vencimiento": forms.TextInput(
                attrs={"class": "form-control my-small-input", "type": "date"}
            ),
            "marca": forms.Select(attrs={"class": "form-select selectpiker"}),
            "clasificacion": forms.Select(attrs={"class": "form-select selectpiker"}),
            "impuesto": forms.Select(attrs={"class": "form-select selectpiker"}),
            "unidad_medida": forms.Select(attrs={"class": "form-select selectpiker"}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductosForms, self).__init__(*args, **kwargs)
        unidades_medida_queryset = UnidadMedida.objects.filter(estado=True)
        self.fields['unidad_medida'].queryset = unidades_medida_queryset
        self.fields['unidad_medida'].widget.choices = [(unidad.id, unidad.descripcion) for unidad in unidades_medida_queryset]

        impuesto_queryset = Impuestos.objects.filter(estado=True)
        self.fields['impuesto'].queryset = impuesto_queryset
        self.fields['impuesto'].widget.choices = [(impuesto.id, impuesto.descripcion) for impuesto in impuesto_queryset]
       
        marca_queryset = Marca.objects.filter(estado = True)
        self.fields['marca'].queryset = marca_queryset
        self.fields['marca'].widget.choices = [(marca.id, marca.descripcion) for marca in marca_queryset]

        clasificacion_queryset = Clasificacion.objects.filter(estado =True)
        self.fields['clasificacion'].queryset = clasificacion_queryset
        self.fields['clasificacion'].widget.choices = [(clasificacion.id, clasificacion.descripcion) for clasificacion in clasificacion_queryset]





