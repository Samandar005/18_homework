from django.urls import path
from . import  views


app_name = 'orders'

urlpatterns = [
    path('list/', views.order_list, name='list'),
    path('detail/<int:pk>/', views.order_detail, name='detail'),

]