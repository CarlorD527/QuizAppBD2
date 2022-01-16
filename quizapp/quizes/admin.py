from django.contrib import admin
from .models import *

class RespuestaEnLinea(admin.TabularInline):
    model = Alternativa

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaEnLinea]

admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Alternativa)
admin.site.register(Curso)
admin.site.register(Examen)
admin.site.register(Tipopregunta)
admin.site.register(Resultado)
admin.site.register(Usuario)