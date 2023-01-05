from django.urls import path 
from base.views import product_views as  views



urlpatterns = [
     path('', views.getProducts, name="products"),
     path('top/', views.getTopProducts, name='top-products'),
     path('all/', views.getAllProducts, name='all-products'),
     path('create/', views.createProduct, name="product-create"),
     path('upload/', views.uploadImage, name="image-upload"),

     path('<str:pk>/', views.getProduct, name="product"),
     path('update/<str:pk>/', views.updateProduct, name="product-update"),
     path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
     
]


#NOTEE: MAKE  SURE CRAETE IS ABOBE <STR:PK> TYPE URLS