from django.urls import path

from .views import (
    homepage, about, product, category, category_summary, ProductListView, ProductDetailView, CategoryListView, CategoryDetailView,
    FileListView, FileDetailView
)


urlpatterns = [
    path('index', homepage, name="home"),
    path('about', about, name='about'),
    path('product/<int:pk>/', product, name='product'),
    path('category/<str:ck>/', category, name='category'),
    path('category_summary', category_summary, name='category'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('products/<int:product_id>/files/', FileListView.as_view(), name='file-list'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail')
]
