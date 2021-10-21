from django.db import models
from datetime import datetime


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre Tipos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Fecha de creacion')
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
