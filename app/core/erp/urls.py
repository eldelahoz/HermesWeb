from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.dashboard.views import DashboardView
from core.erp.views.products.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from core.erp.views.test.view import TestView

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    # Products
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    # Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # Test
    path('tests/', TestView.as_view(), name='tests')
]
