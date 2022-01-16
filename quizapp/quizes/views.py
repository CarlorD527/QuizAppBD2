from django.shortcuts import render
from .models import Examen
from django.views.generic import ListView
# Create your views here.

class VistaListaExamenes(ListView):
    
    model = Examen
    template_name = 'quizes/main.html'

def examen_vista(request,pk):
    examen = Examen.objects.get(pk=pk)

    return render(request, 'quizes/quiz.html',{'obj':examen})