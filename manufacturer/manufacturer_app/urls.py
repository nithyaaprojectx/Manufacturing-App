from django.urls import path
from . import views

urlpatterns = [
    path('', views.manufacturer_list, name='manufacturer_list'),
    path('create/', views.manufacturer_create, name='manufacturer_create'),
]
