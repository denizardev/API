from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno_list, name='aluno_list'),  # Lista todos os alunos
    path('<int:pk>/', views.aluno_detail, name='aluno_detail'),  # Detalhes de um aluno específico
    path('novo/', views.aluno_create, name='aluno_create'),  # Cria um novo aluno (via interface web)
    path('<int:pk>/editar/', views.aluno_update, name='aluno_update'),  # Edita um aluno
    path('<int:pk>/deletar/', views.aluno_delete, name='aluno_delete'),  # Deleta um aluno
]
