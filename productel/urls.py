from django.contrib import admin
from django.urls import path
from productel import views

urlpatterns = [
    path('list/', views.product_list),
    path('create/', views.product_create),
    path('detail/', views.product_detail),
    path('update/', views.product_update),
    path('delete/', views.product_delete),
]
