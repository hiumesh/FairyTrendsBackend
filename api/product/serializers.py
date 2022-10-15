from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from api.product import models

# Base Serializers

class BrandMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.BrandMedia
    fields = ['MediaId', 'MediaLink', 'MediaType']
    read_only_fields = ['MediaId']

class BrandSerializer(WritableNestedModelSerializer):
  class Meta:
    model = models.Brand
    fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Department
    fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Category
    fields = ['CategoryId', 'CategoryName']


# Detailed/Realated Serializers

class DepartmentBrandSerializer(serializers.ModelSerializer):
  department_brands = BrandSerializer(many=True, read_only=True)
  class Meta:
    model = models.Department
    fields = '__all__'

class DepartmentCategorySerializer(serializers.ModelSerializer):
  department_category = CategorySerializer(many=True, read_only=True)
  class Meta:
    model = models.Department
    fields = '__all__'


class BrandWithMediaSerializer(WritableNestedModelSerializer):
  brand_media = BrandMediaSerializer(many=True)
  class Meta:
    model = models.Brand
    fields = '__all__'

class BrandDepartmentSerializer(serializers.ModelSerializer):
  brand_media = BrandMediaSerializer(many=True)
  brand_departments = DepartmentSerializer(source='BrandDepartment', read_only=True, many=True)
  class Meta:
    model = models.Brand
    fields = '__all__'


class CategoryDetailedSerializer(serializers.ModelSerializer):
  department = DepartmentSerializer(source="DepartmentId", read_only=True)
  parent_category = CategorySerializer(source="ParentId", read_only=True)
  class Meta:
    model = models.Category
    fields = '__all__'

class ChildCategoriesSerializer(serializers.ModelSerializer):
  child_category = CategorySerializer(many=True, read_only=True)
  class Meta:
    model = models.Category
    fields = '__all__'



  


""" def create(self, validated_data):
    with transaction.atomic():
      brand_media = validated_data.pop('brand_media')
      brand_departments = []
      for dep in validated_data.pop('BrandDepartment'):
        brand_departments.append(dep.DepartmentId)
      brand_departments = models.Department.objects.filter(DepartmentId__in = brand_departments)
      brand_instance = models.Brand.objects.create(**validated_data)
      brand_instance.BrandDepartment.set(brand_departments)
      for media in brand_media:
        media['BrandId'] = brand_instance
        models.BrandMedia.objects.create(**media)
      return brand_instance """
