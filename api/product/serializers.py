from api.product import models, util
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from queue import Queue

# Tag Serializer
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Tag
    fields = '__all__'

# Category Pair Serializer
class CategoryPairsSerializer(WritableNestedModelSerializer):
  class Meta:
    model = models.CategoryPair
    fields = '__all__'

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Category
    fields = ['Id', 'Name', 'Tags']
    read_only_fields = ['Name', 'Tags']

class CategoryListSerializer(serializers.ModelSerializer):
  parent_category = CategorySerializer(source="ParentId", read_only=True)
  class Meta:
    model = models.Category
    fields = '__all__'
    read_only_fields = ['ParentTree', 'Level']
  
  def validate(self, attrs):
    if (('ParentId' in attrs) and attrs['ParentId']):
      attrs['ParentTree'] = getattr(attrs['ParentId'], 'ParentTree') + '/' + getattr(attrs['ParentId'], 'Name')
      attrs['Level'] = getattr(attrs['ParentId'], 'Level') + 1

      parent_category_instance = models.Category.objects.get(Id=getattr(attrs['ParentId'], 'Id'))
      parent_category_serializer = CategorySerializer(parent_category_instance)
      valid_tags = parent_category_serializer.data['Tags']
      if len(valid_tags):
        """ if (not len(attrs['Tags'])):
          raise serializers.ValidationError("Tags cannot be empty") """
        for tag in attrs['Tags']:
          if (getattr(tag, 'Id') not in valid_tags):
            raise serializers.ValidationError("Tags can be only from parent Category Tags")
    return super().validate(attrs)

class CategoryDetailedSerializer(WritableNestedModelSerializer):
  direct_children = CategorySerializer(many=True, read_only=True)
  all_children = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = models.Category
    fields = '__all__'
  def get_all_children(self, obj):
    children = list()
    q = Queue(maxsize = 0)
    q.put(getattr(obj,'Id'))
    while not q.empty():
      category_id = q.get()
      for child in models.Category.objects.filter(ParentId=category_id):
        q.put(getattr(child, 'Id'))
        children.append(
          {
            'Id' : getattr(child, 'Id'),
            'Name': getattr(child, 'Name')
          })
    return children

# Collection and CollectionCategories Serializer
class CollectionCategoriesSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    if 'Alias' not in validated_data or not validated_data['Alias']:
      validated_data['Alias'] = getattr(validated_data['CategoryId'], 'Name')
    return super().create(validated_data)
  class Meta:
    model = models.CollectionCategories
    exclude = ['CollectionId']

class CollectionListSerializer(WritableNestedModelSerializer):
  class Meta:
    model = models.Collection
    fields = '__all__'

class CollectionCategoriesCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.CollectionCategories
    fields = '__all__'

class CollectionDetailedSerializer(WritableNestedModelSerializer):
  collection_categories = CollectionCategoriesSerializer(many=True)
  collection_category_pairs = CategoryPairsSerializer(source="CategoryPairs", read_only=True, many=True)
  class Meta:
    model = models.Collection
    exclude = ['Categories']

  def update(self, instance, validated_data):
    models.CategoryCollectionCategories.objects.filter(Id=getattr(instance, 'Id')).delete()
    collection_categories = validated_data['collection_categories']
    for category in collection_categories:
      util.update_category_collection_category(category, instance, category_serializer=CategorySerializer, category_collection_categories_create_serializer=CollectionCategoriesCreateSerializer)
    del validated_data['collection_categories']
    return super().update(instance, validated_data)


# Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Department
    fields = '__all__'

class DepartmentDetailedSerializer(serializers.ModelSerializer):
  department_collections = CollectionDetailedSerializer(source="Collections", read_only=True, many=True)
  class Meta:
    model = models.Department
    exclude = ['Collections']


# Brand Serializer
class BrandMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.BrandMedia
    fields = ['MediaId', 'MediaLink', 'MediaType']
    read_only_fields = ['MediaId']

class BrandSerializer(WritableNestedModelSerializer):
  class Meta:
    model = models.Brand
    fields = '__all__'

class BrandWithMediaSerializer(WritableNestedModelSerializer):
  brand_media = BrandMediaSerializer(many=True)
  class Meta:
    model = models.Brand
    fields = '__all__'


# Attribute Serializer
class AttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Attributes
    fields = '__all__'


# Product Serialzer
class ProductMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ProductMedia
    fields = ['MediaId', 'MediaLink', 'MediaType']
    read_only_fields = ['MediaId']

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Product
    fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ProductDetail
    fields = ['ProductDetailId', 'ProductId', 'AttributeName', 'AttributeLevel', 'AttributeValue']
    read_only_fields = ['ProductDetailId', 'ProductId']

class ProductCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ProductCategory
    fields = ['ProductCategoryId', 'ProductId', 'Id']
    read_only_fields = ['ProductCategoryId', 'ProductId']

class ProductCategoryAttributeValueSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ProductCategoryAttributeValue
    fields = ['ProductCategoryAttributeValueId', 'ProductCategoryId', 'AttributeId', 'AttributeValue']
    read_only_fields = ['ProductCategoryAttributeValueId', 'ProductCategoryId']

class ProductListSerializer(serializers.ModelSerializer):
  product_media = ProductMediaSerializer(many=True)
  class Meta:
    model = models.Product
    fields = '__all__'

class ProductDetailedSerializer(serializers.ModelSerializer):
  product_media = ProductMediaSerializer(many=True)
  product_detail = ProductDetailSerializer(many=True)
  product_category = ProductCategorySerializer(many=True)
  class Meta:
    model = models.Product
    fields = '__all__'

class ProductCategoryForCreateSerializer(WritableNestedModelSerializer):
  product_category_attributes = ProductCategoryAttributeValueSerializer(many=True)
  class Meta:
    model = models.ProductCategory
    fields = ['ProductCategoryId', 'ProductId', 'Id', 'product_category_attributes']
    read_only_fields = ['ProductCategoryId', 'ProductId']

class ProductCreateSerializer(WritableNestedModelSerializer):
  product_media = ProductMediaSerializer(many=True)
  product_detail = ProductDetailSerializer(many=True)
  product_category = ProductCategoryForCreateSerializer(many=True)
  class Meta:
    model = models.Product
    fields = '__all__'


  """ def validate(self, attrs):
    print(attrs['collection_categories'])
    category_serilizer = CategoryDetailedSerializer(attrs['PrimeCategory'])
    valid_children = list()
    for child in category_serilizer['all_children'].value:
      valid_children.append(child['Id'])
    for child in attrs['collection_categories']:
      if getattr(child['Id'], 'Id') not in valid_children:
        raise serializers.ValidationError("Not a valid list of Collection Categories")
    return super().validate(attrs) """