# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('add/', views.add_item, name='add_item'),  # Add item URL pattern
    path('get_item_details/<int:item_id>/', views.get_item_details, name='get_item_details'),  # Add URL pattern for item details


]