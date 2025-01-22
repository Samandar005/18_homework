from django.urls import path
from . import  views


app_name = 'categories'

urlpatterns = [
    path('create/', views.category_create, name='create'),
    path('list/', views.category_list, name='list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.category_detail, name='detail'),
    path('category/<int:pk>/update/', views.category_update, name='update'),
    path('delete/<int:pk>/', views.category_delete, name='delete'),
]