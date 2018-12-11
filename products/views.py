from django.shortcuts import render
from products.models import Product, ProductDetail
from products.serializers import ProductSerializer, ProductDetailSerializer
from rest_framework import generics
# Create your views here.

class ProductDetailList(generics.ListCreateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    

class ProductDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
