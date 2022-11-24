from django.db import models

class Tag(models.Model):
  Id = models.BigAutoField(primary_key=True)
  Name = models.CharField(max_length=256, null=False, unique=True)
  
  def __str__(self):
    return self.Name

class Attributes(models.Model):
  Id = models.BigAutoField(primary_key=True)
  Name = models.CharField(max_length=256, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.Name


class Category(models.Model):
  Id = models.BigAutoField(primary_key=True)
  ParentId = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='direct_children')
  ParentTree = models.CharField(max_length=700)
  Name = models.CharField(max_length=256, unique=True)
  Level = models.SmallIntegerField(default=0)
  Attributes = models.ManyToManyField(Attributes, related_name='attribute_categories')
  Tags = models.ManyToManyField(Tag, related_name='tag_categories', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.Name

class CategoryPair(models.Model):
  Id = models.BigAutoField(primary_key=True)
  Name = models.CharField(max_length=700, unique=True)
  Alias = models.CharField(max_length=256, null=True, default=None)
  Categories = models.ManyToManyField(Category, related_name='category_in_pairs')
  Tags = models.ManyToManyField(Tag, related_name='tag_in_pairs', blank=True)

  def __str__(self) -> str:
    return self.Name

class Collection(models.Model):
  Id = models.BigAutoField(primary_key=True)
  Name = models.CharField(max_length=256, unique=True)
  Alias = models.CharField(max_length=256, null=True, default=None)
  Categories = models.ManyToManyField(Category, through='CollectionCategories', related_name='collection_categories')
  CategoryPairs = models.ManyToManyField(CategoryPair, related_name='category_pairs_collection', blank=True)
  
  def __str__(self):
    return self.Name

class CollectionCategories(models.Model):
  CollectionCategoryId = models.BigAutoField(primary_key=True)
  CollectionId = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='collection_categories')
  CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
  Alias = models.CharField(max_length=256, null=True, default=None)
  Tags = models.ManyToManyField(Tag, related_name='category_collection_category_tag', blank=True)

class Department(models.Model):
  Id = models.BigAutoField(primary_key=True)
  Name = models.CharField(max_length=256, unique=True)
  Collections = models.ManyToManyField(Collection, related_name='department_category_collections')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.Name

class Brand(models.Model):
  BrandId = models.BigAutoField(primary_key=True)
  BrandName = models.CharField(max_length=256, unique=True)
  BrandDescription = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.BrandName

class BrandMedia(models.Model):
  MEDIA_TYPES = (
    ('LO', 'Logo'),
    ('IM', 'Image'),
  )

  MediaId = models.BigAutoField(primary_key=True)
  BrandId = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_media')
  MediaLink = models.URLField(max_length=500)
  MediaType = models.CharField(max_length=2, choices=MEDIA_TYPES)

  def __str__(self):
    return self.MediaLink

class Product(models.Model):
  ProductId = models.BigAutoField(primary_key=True)
  ProductName = models.CharField(max_length=1000, unique=True)
  ProductDescription = models.TextField()
  Price = models.DecimalField(max_digits=10, decimal_places=2)
  ProductRating = models.DecimalField(decimal_places=1, max_digits=2)
  BrandId = models.ForeignKey(Brand, on_delete=models.CASCADE)
  Active = models.BooleanField(default=True)
  RedirectURL = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.ProductName

class ProductDetail(models.Model):
  ProductDetailId = models.BigAutoField(primary_key=True)
  ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail')
  AttributeName = models.CharField(max_length=256, null=True)
  AttributeLevel = models.SmallIntegerField()
  AttributeValue = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class ProductMedia(models.Model):
  MEDIA_TYPES = (
    ('IM', 'Image'),
    ('VD', 'Video'),
  )
  MediaId = models.BigAutoField(primary_key=True)
  ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_media')
  MediaLink = models.URLField()
  MediaType = models.CharField(max_length=2, choices=MEDIA_TYPES)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.MediaLink

class ProductCategory(models.Model):
  ProductCategoryId = models.BigAutoField(primary_key=True)
  ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_category')
  CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
  Tags = models.ManyToManyField(Tag, related_name='product_category_tag')

class ProductCategoryAttributeValue(models.Model):
  ProductCategoryAttributeValueId = models.BigAutoField(primary_key=True)
  ProductCategoryId = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='product_category_attributes')
  AttributeId = models.ForeignKey(Attributes, on_delete=models.CASCADE)
  AttributeValue = models.TextField()
