from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_usuario, name='add'),
    path('edit/<int:id_usuario>/', views.edit_usuario, name='edit'),
    path('delete/<int:id_usuario>/', views.delete_usuario, name='delete'),
]