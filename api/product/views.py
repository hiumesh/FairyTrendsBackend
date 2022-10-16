from rest_framework import generics, serializers

from api.product import models
from api.product import serializers


# Department Views

class DepartmentListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Department.objects.all()
  serializer_class = serializers.DepartmentSerializer

department_list_create_view = DepartmentListCreateAPIView.as_view()

class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Department.objects.all()
  serializer_class = serializers.DepartmentSerializer
  lookup_field = 'DepartmentId'

department_retrieve_update_destory_view = DepartmentRetrieveUpdateDestroyAPIView.as_view()

class DepartmentBrandListAPIView(generics.ListAPIView):
  queryset = models.Department.objects.all()
  serializer_class = serializers.DepartmentBrandSerializer

department_brand_list_view = DepartmentBrandListAPIView.as_view()

class DepartmentBrandRetrieveAPIView(generics.RetrieveAPIView):
  queryset = models.Department.objects.all()
  serializer_class = serializers.DepartmentBrandSerializer
  lookup_field = 'DepartmentId'

department_brand_retrieve_view = DepartmentBrandRetrieveAPIView.as_view()

class DepartmentCategoryListAPIView(generics.ListAPIView):
  queryset = models.Department.objects.all()
  serializer_class = serializers.DepartmentCategorySerializer

department_category_list_view = DepartmentCategoryListAPIView.as_view()

class DepartmentCategoryRetrieveAPIView(generics.RetrieveAPIView):
  queryset = models.Department.objects.all()
  serializer_class = serializers.DepartmentCategorySerializer
  lookup_field = 'DepartmentId'

department_category_retrieve_view = DepartmentCategoryRetrieveAPIView.as_view()


# Brand Views

class BrandListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.BrandWithMediaSerializer

brand_list_create_view = BrandListCreateAPIView.as_view()

class BrandRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.BrandWithMediaSerializer
  lookup_field = 'BrandId'

brand_retrieve_update_destory_view = BrandRetrieveUpdateDestoryAPIView.as_view()

class BrandDepartmentListAPIView(generics.ListAPIView):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.BrandDepartmentSerializer

brand_department_list_view = BrandDepartmentListAPIView.as_view()

class BrandDepartmentRetrieveAPIView(generics.RetrieveAPIView):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.BrandDepartmentSerializer
  lookup_field = 'BrandId'

brand_department_retrieve_view = BrandDepartmentRetrieveAPIView.as_view()



# Category Views

class CategoryListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Category.objects.all()
  serializer_class = serializers.CategoryDetailedSerializer

category_list_create_view = CategoryListCreateAPIView.as_view()

class CategoryRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Category.objects.all()
  serializer_class = serializers.CategoryDetailedSerializer
  lookup_field = 'CategoryId'

category_retrieve_update_view = CategoryRetrieveUpdateDestoryAPIView.as_view()

class ChildCategoriesListAPIView(generics.ListAPIView):
  queryset = models.Category.objects.all()
  serializer_class = serializers.ChildCategoriesSerializer

child_categories_list_view = ChildCategoriesListAPIView.as_view()

class ChildCategoriesRetrieveAPIView(generics.RetrieveAPIView):
  queryset = models.Category.objects.all()
  serializer_class = serializers.ChildCategoriesSerializer
  lookup_field = 'CategoryId'

child_categories_retrieve_view = ChildCategoriesRetrieveAPIView.as_view()


# Attribute Views

class AttributeListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Attributes.objects.all()
  serializer_class = serializers.AttributeListSerializer

attribute_list_create_view = AttributeListCreateAPIView.as_view()

class AttributeRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Attributes.objects.all()
  serializer_class = serializers.AttributeWithValuesAndCategorySerializer
  lookup_field = 'AttributeId'

attribute_retrieve_update_destory_view = AttributeRetrieveUpdateDestoryAPIView.as_view()

class AttributeValueListAPIView(generics.ListAPIView):
  queryset = models.Attributes.objects.all()
  serializer_class = serializers.AttributeWithValuesSerializer

attribute_list_view = AttributeValueListAPIView.as_view()

class AttributeValueRetrieveAPIView(generics.RetrieveAPIView):
  queryset = models.Attributes.objects.all()
  serializer_class = serializers.AttributeWithValuesSerializer
  lookup_field = 'AttributeId'

attribute_retrieve_view = AttributeValueRetrieveAPIView.as_view()
