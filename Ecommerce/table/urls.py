from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.apiOverview, name = "table-overview"),
    # Get all categories samples. 
    path('categories_list/', views.CategoriesList, name='categories_list'),
    # Get all products samples. 
    path('product_list/', views.ProductList, name= 'product_list')
    
]