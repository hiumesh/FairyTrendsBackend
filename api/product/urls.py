from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.product import views
from api.product import viewset

router = DefaultRouter()

router.register('product', viewset.ProductViewSet, basename='product')
router.register('attribute', viewset.AttributesViewSet)
router.register('department', viewset.DepartmentViewSet)
router.register('brand', viewset.BrandViewSet)
router.register('category', viewset.CategoryViewSet)
router.register('collection', viewset.Collection)
router.register('tag', viewset.TagViewSet)
router.register('categorypair', viewset.CategoryPairViewSet)

urlpatterns = [
  path('', include(router.urls)),
]