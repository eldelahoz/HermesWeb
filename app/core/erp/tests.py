# from django.test import TestCase
from config.wsgi import *
from core.erp.models import Category
# from core.erp.models import Type

# Create your tests here.

# Type(name='Prueba').save()
# Type(name='Viba').save()
# Type(name='Montana').save()

# print(Type.objects.all())

# f = Type.objects.filter(name__icontains='adm')
# f = Type.objects.filter(name__startswith='A')
# f = Type.objects.filter(name__in=['Presidente', 'Administrador']).count()
# f = Type.objects.filter(name__icontains='Presidente').query
# f = Type.objects.filter(name__endswith='a').exclude(id=5)
# print(f)

# for i in Type.objects.filter(name__endswith='a')[2:]:
#    print(i.name)
print(Category.objects.all())
if Category.objects.filter(name__in=['Bebidas']):
    print("Si existe")
else:
    print("No existe")