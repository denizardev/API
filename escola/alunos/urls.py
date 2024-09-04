#from django.urls import path
#from . import views

#urlpatterns = [
    #path('', views.aluno_list, name='aluno_list'),
    #path('<int:pk>/', views.aluno_detail, name='aluno_detail'),
    #path('novo/', views.aluno_create, name='aluno_create'),
    #path('<int:pk>/editar/', views.aluno_update, name='aluno_update'),
    #path('<int:pk>/deletar/', views.aluno_delete, name='aluno_delete'),
#]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno_list, name='aluno_list'),
    path('<int:pk>/', views.aluno_detail, name='aluno_detail'),
    path('novo/', views.aluno_create, name='aluno_create'),
    path('<int:pk>/editar/', views.aluno_update, name='aluno_update'),
    path('<int:pk>/deletar/', views.aluno_delete, name='aluno_delete'),
    
]

