from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-info/', views.contact_info, name='contact_info'),
]