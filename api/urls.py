from django.urls import path, include

urlpatterns = [
  path('productAPI/', include('api.product.urls')),
]
