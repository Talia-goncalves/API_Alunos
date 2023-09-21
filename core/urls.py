from django.contrib import admin
from django.urls import path
from controleTarefas.views.alunosView import AlunosView
from controleTarefas.views.disciplinasView import DisciplinasView
from controleTarefas.views.tarefasView import TarefasView
from controleTarefas.views.alunosTarefasView import AlunoTarefasView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', AlunosView.as_view()),
    path('api/alunos/<int:pk>/', AlunosView.as_view()),
    path('api/disciplinas/', DisciplinasView.as_view()),
    path('api/disciplinas/<int:pk>/', DisciplinasView.as_view()),
    path('api/tarefas/', TarefasView.as_view()),
    path('api/tarefas/<int:pk>/', TarefasView.as_view()),
    path('api/alunos/<int:pk>/tarefas/', AlunoTarefasView.as_view()),
]
