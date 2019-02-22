from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),
    path('new/', views.shop_new, name='shop_new'),
    path('new_cbv/', views.shop_new_cbv, name='shop_new_cbv'),
    path('edit/<int:pk>/', views.shop_edit, name='shop_edit'),
    path('edit_cbv/<int:pk>/', views.shop_edit_cbv, name='shop_edit_cbv'),
    path('delete/<int:pk>/', views.shop_delete),
]
