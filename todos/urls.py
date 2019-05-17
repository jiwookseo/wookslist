from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "todos"
urlpatterns = [
    path('', TemplateView.as_view(template_name='todos/app.html'), name="index"),
    path('lists/', views.lists_list, name="lists_list"),
    path('lists/<int:pk>/', views.lists_detail, name="lists_detail"),
    path('todos/', views.todos_list, name="todos_list"),
    path('todos/<int:pk>/', views.todos_detail, name="todos_detail"),
    path('todos/<int:pk>/details/', views.details_list, name="details_list"),
    path('details/<int:pk>/', views.details_detail, name="details_detail"),
]
