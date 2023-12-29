from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product, ProductLine
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductLineSerializer,
    ProductSerializer,
)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def list(self, queryset):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path=r"category/(?P<category>\w+)/all")
    def list_product_by_category(self, queryset, category):
        # adds this comments text to swagger ui
        """
        Returns all products related to a category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)


class ProductLineViewSet(viewsets.ViewSet):
    queryset = ProductLine.objects.all()

    @extend_schema(responses=ProductLineSerializer)
    def list(self, queryset):
        serializer = ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)
