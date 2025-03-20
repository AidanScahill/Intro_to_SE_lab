from django.urls import path 
from userauth import views

urlpatterns = [
    path('sign-up/', views.register_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
]