from django.urls import path
from .views import index, PostListCreateAPIView, formulario

urlpatterns = [
    path('', index, name='blog-index'),  # URL para o frontend
    path('api/posts/', PostListCreateAPIView.as_view(), name='blog-api'),  # URL para a API
    path('formulario/', formulario, name='blog-formulario')  # URL para o formulário
]
