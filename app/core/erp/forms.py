from django.core import validators
from django.forms import *
from django.forms import CharField
from core.erp.models import Category, Product


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

    # def clean(self):
    #    cleanded = super().clean()

    # if len(cleanded['name']) < 50:
    # self.add_error('name', 'Le faltan caracteres')
    #    raise forms.ValidationError('Validacion test')
    # print(cleanded)
    #    return cleanded
