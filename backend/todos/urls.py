from django.urls import URLPattern, path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view()),
    path("", ListTodo.as_view()),
]