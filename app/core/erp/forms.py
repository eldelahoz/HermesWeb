from datetime import datetime

from django.core import validators
from django.forms import *
from core.erp.models import Category, Product, Client


# def validate_nombre(value):
#     if len(value) < 50:
#         raise ValidationError('%(value)s le faltan', params={'value': value})


class CategoryForm(ModelForm):
    # name = CharField(validators=[validate_nombre])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})
            form.field.widget.attrs.update({'autocomplete': 'off'})
        self.fields['name'].widget.attrs.update({'autofocus': True})

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'columns': 3
                }
            )
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = e
        return data

    # def clean(self):
    #     cleanded = super().clean()
    #
    #     if len(cleanded['name']) < 50:
    #         self.add_error('name', 'Le faltan caracteres')
    #         raise forms.ValidationError('Validacion test')
    #     print(cleanded)
    #     return cleanded


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})
            form.field.widget.attrs.update({'autocomplete': 'off'})
        self.fields['nombre'].widget.attrs.update({'autofocus': True})

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'cat': 'Categoria',
            'pvp': 'Precio de venta'
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    # def clean(self):
    #    cleanded = super().clean()

    # if len(cleanded['name']) < 50:
    # self.add_error('name', 'Le faltan caracteres')
    #    raise forms.ValidationError('Validacion test')
    # print(cleanded)
    #    return cleanded


class ClientForm(ModelForm):
    fecha_nac = DateField(initial=datetime.now,
        widget=DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})
            form.field.widget.attrs.update({'autocomplete': 'off'})
        self.fields['nombres'].widget.attrs.update({'autofocus': True})

    class Meta:
        model = Client
        fields = '__all__'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control select2'
    }))

    products = ModelChoiceField(queryset=Category.objects.none(), widget=Select(attrs={
        'class': 'form-control'
    }))
