from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.http import JsonResponse    
from django.shortcuts import render, HttpResponse
from django.db import connection
import cx_Oracle
# Create your views here.

class VistaListaExamenes(ListView):
    
    model = Examen
    template_name = 'quizes/main.html'

def examen_vista(request,pk):
    examen = Examen.objects.get(pk=pk)

    return render(request, 'quizes/quiz.html',{'obj':examen})

def quiz_data_view(request, pk):
    quiz = Examen.objects.get(pk=pk)
    questions = []
    for q in quiz.get_preguntas():
        answers = []
        for a in q.get_respuestas():
            answers.append(a.titulo)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.duracion,
    })


def save_quiz_view(request, pk):
    
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            id_pregunta = Pregunta.objects.get(titulo=k)
            questions.append(id_pregunta)
        print(questions)

        user = Usuario.objects.get(pk=pk)
        quiz = Examen.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.numero_preguntas 
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.titulo)

            if a_selected != "":
                question_answers = Alternativa.objects.filter(id_pregunta=q)
                for a in question_answers:
                    if a_selected == a.titulo:
                        if a.correcta:
                            score += 1
                            correct_answer = a.titulo
                    else:
                        if a.correcta:
                            correct_answer = a.titulo

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
       
        score_ = score * multiplier
        score_final = (score_ / 100 ) * 20
        Resultado.objects.create(id_usuario= user, id_examen=quiz, nota=score_final)

        if score_ >= quiz.puntaje_requerido:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})

def cursos_view(request):
    data = {
        'cursos':listado_cursos()
    }
    nombre = request.POST.get('nombre')
    if request.method == 'POST' and nombre!='':
        salida = agregar_curso(nombre)
        nombre = ''
        if salida == 1:
                data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha podido guardar'
  
    return render(request, 'quizes/cursos.html',data)

def listado_cursos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_CURSOS",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def agregar_curso(nombre):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CURSO', [nombre,salida])
    return salida.getvalue()