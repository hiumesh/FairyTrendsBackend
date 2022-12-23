from django.contrib import admin
from api.product import models

admin.site.register(models.Product)
admin.site.register(models.Attributes)
admin.site.register(models.Department)
admin.site.register(models.Brand)
admin.site.register(models.BrandMedia)
admin.site.register(models.Category)
admin.site.register(models.Collection)
admin.site.register(models.CollectionCategories)
admin.site.register(models.ProductDetail)
admin.site.register(models.ProductMedia)
admin.site.register(models.ProductCategoryAttributeValue)
admin.site.register(models.ProductCategory)

