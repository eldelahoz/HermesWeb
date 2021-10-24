from django.shortcuts import render
from core.erp.models import Category, Product
# Create your views here.


def myfirstview(request):
    data = {
        'name' : 'DelaHoz',
        'categorias': Category.objects.all()
    }
    return render(request, 'index.html', data) # JsonResponse(data) HttpResponse("Bonjour les amis")


def mysecondview(request):
    data = {
        'name' : 'DelaHoz',
        'categorias': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data) # JsonResponse(data) HttpResponse("Bonjour les amis")
