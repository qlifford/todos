from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todoList'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('deleteTodo/<str:id>/', views.deleteTodo, name='deleteTodo'),
    path('updateTodo/<str:id>/', views.updateTodo, name='updateTodo'),
]
