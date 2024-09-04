from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .serializers import AlunoSerializer
from .forms import AlunoForm  # Certifique-se de que o formulário AlunoForm esteja definido

# Funções para a API REST
@api_view(['GET'])
def get_alunos(request):
    alunos = Aluno.objects.all()
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def criar_aluno(request):
    serializer = AlunoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_aluno(request, id):
    try:
        aluno = Aluno.objects.get(pk=id)
    except Aluno.DoesNotExist:
        return Response({"error": "Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AlunoSerializer(aluno)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Funções para as Views Tradicionais
def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno_list.html', {'alunos': alunos})

def aluno_detail(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno_detail.html', {'aluno': aluno})

def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'aluno_form.html', {'form': form})

def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'aluno_update.html', {'form': form})

def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    return render(request, 'aluno_delete.html', {'aluno': aluno})

def home(request):
    return render(request, 'home.html')
