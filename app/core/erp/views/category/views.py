from django.shortcuts import render
from django.views.generic import ListView

from core.erp.models import Category, Product


def category_list(request):
    data = {
        'title': 'Listado Categoria',
        'categorias': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='L')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Categoria'
        # context['products'] = Product.objects.all()
        return context
