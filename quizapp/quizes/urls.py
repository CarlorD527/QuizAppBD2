from django.urls import path

from .views import (
    VistaListaExamenes,
    examen_vista
)


app_name = 'quizes'

urlpatterns = [
    path('',VistaListaExamenes.as_view(),name = 'vista-principal'),
    path('<pk>/',examen_vista ,name ='vista-examen'),
]