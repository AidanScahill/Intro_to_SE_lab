from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_filter/<slug:category_slug>/', views.product_filter, name='product_filter'),
    path('product_detail/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('product_search/', views.product_search, name='product_search'),
    path('seller_panel/', views.seller_panel, name='seller_panel'),
    path('product_edit/<slug:product_slug>/', views.product_edit, name='product_edit'),
    path('product_add/', views.product_add, name='product_add'),
    

]