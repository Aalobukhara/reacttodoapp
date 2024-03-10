# todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoItemListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', views.TodoItemDetailView.as_view(), name='todo-item-detail'),
]