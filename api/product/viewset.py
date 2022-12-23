from rest_framework import viewsets

from api.product import models
from api.product import serializers
from api.product import util

LOOKUP_VALUE_REGEX = "[^/]+"

class TagViewSet(viewsets.ModelViewSet):
  queryset = models.Tag.objects.all()
  serializer_class = serializers.TagSerializer
  lookup_field = 'Id'
  lookup_value_regex = LOOKUP_VALUE_REGEX

class DepartmentViewSet(util.MultiSerializerViewSet):
  queryset = models.Department.objects.all()
  serializers = {
    'default': None,
    'list': serializers.DepartmentSerializer,
    'retrieve':  serializers.DepartmentDetailedSerializer, 
    'create': serializers.DepartmentSerializer,
    'update': serializers.DepartmentSerializer,
    'partial_update': serializers.DepartmentSerializer,
  }
  lookup_field = 'Name'
  lookup_value_regex = LOOKUP_VALUE_REGEX

class CategoryViewSet(util.MultiSerializerViewSet):
  queryset = models.Category.objects.all()
  serializers = {
    'default': None,
    'list': serializers.CategoryListSerializer,
    'retrieve':  serializers.CategoryDetailedSerializer, 
    'create': serializers.CategoryListSerializer,
    'update': serializers.CategoryListSerializer,
    'partial_update': serializers.CategoryListSerializer,
  }
  lookup_field = 'Id'
  lookup_value_regex = LOOKUP_VALUE_REGEX

class CategoryPairViewSet(viewsets.ModelViewSet):
  queryset = models.CategoryPair.objects.all()
  serializer_class = serializers.CategoryPairsSerializer
  lookup_field = 'Id'
  lookup_value_regex = LOOKUP_VALUE_REGEX

class Collection(util.MultiSerializerViewSet):
  queryset = models.Collection.objects.all()
  serializers = {
    'default': None,
    'list': serializers.CollectionListSerializer,
    'retrieve':  serializers.CollectionDetailedSerializer, 
    'create': serializers.CollectionDetailedSerializer,
    'update': serializers.CollectionDetailedSerializer,
    'partial_update': serializers.CollectionDetailedSerializer,
  }
  lookup_field = 'Id'
  lookup_value_regex = LOOKUP_VALUE_REGEX

class BrandViewSet(viewsets.ModelViewSet):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.BrandWithMediaSerializer
  lookup_field = 'BrandId'
  lookup_value_regex = LOOKUP_VALUE_REGEX

class AttributesViewSet(viewsets.ModelViewSet):
  queryset = models.Attributes.objects.all()
  serializer_class = serializers.AttributeSerializer
  lookup_field = 'AttributeId'
  lookup_value_regex = "[^/]+" 

class ProductViewSet(util.MultiSerializerViewSet):
  queryset = models.Product.objects.all()
  serializers = {
    'default': None,
    'list': serializers.ProductListSerializer,
    'retrieve':  serializers.ProductDetailedSerializer, 
    'create': serializers.ProductCreateSerializer,
  }
  