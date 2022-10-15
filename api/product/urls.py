from django.urls import path

from api.product import views

urlpatterns = [
  path('department/', views.department_list_create_view),
  path('department/<int:DepartmentId>/', views.department_retrieve_update_destory_view),
  path('department_brand/', views.department_brand_list_view),
  path('department_brand/<int:DepartmentId>/', views.department_brand_retrieve_view),
  path('department_category/', views.department_category_list_view),
  path('department_category/<int:DepartmentId>/', views.department_category_retrieve_view),

  path('brand/', views.brand_list_create_view),
  path('brand/<int:BrandId>/', views.brand_retrieve_update_destory_view),
  path('brand_department/', views.brand_department_list_view),
  path('brand_department/<int:BrandId>/', views.brand_department_retrieve_view),

  path('category/', views.category_list_create_view),
  path('category/<int:CategoryId>/', views.category_retrieve_update_view),
  path('category_child/', views.child_categories_list_view),
  path('category_child/<int:CategoryId>/', views.child_categories_retrieve_view)
]