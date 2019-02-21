from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.shop_detail),
    path('new/', views.shop_new),
    path('new_cbv/', views.shop_new_cbv),
    # path('<int:pk>/', views.shop_edit),
    # path('<int:pk>/', views.shop_delete),
]
