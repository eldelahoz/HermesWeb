from config.wsgi import *
from core.erp.models import Category
import random

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
# print(Category.objects.all())
# if Category.objects.filter(name__in=['Bebidas']):
#     print("Si existe")
# else:
#     print("No existe")

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azucar y dulces',
        'Grasas, aceite y mantequilla']


# letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(1, 6000):
#     name = ''.join(random.choices(letter, k=5))
#     while Category.objects.filter(name=name).exists():
#         name = ''.join(random.choices(letter, k=5))
#     Category(name=name).save()
#     print(f"Guardado registro {i}")
