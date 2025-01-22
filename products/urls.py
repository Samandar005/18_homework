from django.urls import path
from . import  views


app_name = 'products'

urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('list/', views.product_list, name='list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.product_detail, name='detail'),
    path('category/<int:pk>/update/', views.product_update, name='update'),
    path('delete/<int:pk>/', views.product_delete, name='delete'),
]