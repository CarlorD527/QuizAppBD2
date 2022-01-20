from unicodedata import name
from django import views
from django.urls import path
from .views import (
    VistaListaExamenes,
    examen_vista,
    quiz_data_view,
    save_quiz_view,
    cursos_view,
    eliminar_curso
)
from . import views

app_name = 'quizes'

urlpatterns = [
    path('',VistaListaExamenes.as_view(),name = 'vista-principal'),
    path('<int:pk>/',examen_vista ,name ='vista-examen'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('cursos/',  cursos_view, name='cursos_view'),
    path('cursos/eliminar_curso/<pk>/',views.eliminar_curso)
]