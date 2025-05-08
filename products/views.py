from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category, File
from .API import global_price, brazil_price, turkey_price
from .serializers import ProductSerializer, CategorySerializer, FileSerializer


def homepage(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})


def about(request):
    return render(request, 'about.html')


def product(request, pk):
    product = Product.objects.get(product_id=pk)
    product_id = str(pk)
    price1 = global_price(product_id)
    price2 = turkey_price(product_id)
    price3 = brazil_price(product_id)
    return render(request, 'product.html', {'product': product, 'price1': price1, 'price2': price2, 'price3': price3})


def category(request, ck):
    try:
        target = get_object_or_404(Category, title=ck)
        products = Product.objects.filter(categories=target)
        return render(request, 'category.html', {'products': products, 'target': target})
    except:
        messages.success(request, "something went wrong!")
        return redirect('home')



class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):

    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self, request, product_id, pk):
        try:
            f = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(f, context={'request': request})
        return Response(serializer.data)
