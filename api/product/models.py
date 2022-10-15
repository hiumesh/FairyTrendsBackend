from django.db import models

class Department(models.Model):
  DepartmentId = models.BigAutoField(primary_key=True)
  DepartmentName = models.CharField(max_length=256, unique=True)
  DepartmentDescription = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.DepartmentName

class Brand(models.Model):
  BrandId = models.BigAutoField(primary_key=True)
  BrandName = models.CharField(max_length=256, unique=True)
  BrandDepartment = models.ManyToManyField(Department,  related_name='department_brands')
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
  ProductName = models.CharField(max_length=256, unique=True)
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
  ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
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
  ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
  MediaLink = models.URLField()
  MediaType = models.CharField(max_length=2, choices=MEDIA_TYPES)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.MediaLink


class Category(models.Model):
  CategoryId = models.BigAutoField(primary_key=True)
  ParentId = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='child_category')
  CategoryName = models.CharField(max_length=256)
  DepartmentId = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_category')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.CategoryName

class Attributes(models.Model):
  AttributeId = models.BigAutoField(primary_key=True)
  AttributeName = models.CharField(max_length=256, null=False)
  Description = models.CharField(max_length=700)
  CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.AttributeName

class AttributeValue(models.Model):
  AttributeValueId = models.BigIntegerField(primary_key=True)
  AttributeId = models.ForeignKey(Attributes, on_delete=models.CASCADE)
  AttributeValue = models.CharField(max_length=256)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.AttributeId}: {self.AttributeValue}"

class ProductCategory(models.Model):
  ProductCategoryId = models.BigAutoField(primary_key=True)
  ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
  CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class ProductCategoryAttributeValue(models.Model):
  ProductCategoryId = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
  AttributeValueId = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)