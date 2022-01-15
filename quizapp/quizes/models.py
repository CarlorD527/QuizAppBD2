# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alternativa(models.Model):
 
    id_alternativa = models.AutoField(primary_key=True)
    id_pregunta = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='id_pregunta', blank=True, null=True)
    titulo = models.CharField(max_length=200)
    correcta = models.BooleanField()
    fecha_creacion = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.titulo
    class Meta:
        managed = False
        db_table = 'alternativa'

class Comentario(models.Model):
    id_comentario = models.BigIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='id_publicacion', blank=True, null=True)
    mensaje = models.CharField(max_length=200)
    puntuacion = models.BigIntegerField()
    foto_solucion = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'comentario'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=200)

    
    def __str__(self):
        return self.nombre_curso

    class Meta:
        managed = False
        db_table = 'curso'

class Examen(models.Model):

    id_examen = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    titulo = models.CharField(max_length=120, blank=True, null=True)
    numero_preguntas = models.BigIntegerField(blank=True, null=True)
    puntaje_requerido = models.BigIntegerField()
    duracion = models.BigIntegerField()

    def __str__(self):
        return self.titulo

    class Meta:
        managed = False
        db_table = 'examen'


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    id_examen = models.ForeignKey(Examen, models.DO_NOTHING, db_column='id_examen', blank=True, null=True)
    id_tipo_pregunta = models.ForeignKey('Tipopregunta', models.DO_NOTHING, db_column='id_tipo_pregunta', blank=True, null=True)
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.titulo
    class Meta:
        managed = False
        db_table = 'pregunta'


class Publicacion(models.Model):
    id_publicacion = models.BigIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.CharField(max_length=400)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'publicacion'


class Tipopregunta(models.Model):
    id_tipo_pregunta = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo
    class Meta:
        managed = False
        db_table = 'tipopregunta'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    correo = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuarioexamen(models.Model):
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_examen = models.ForeignKey(Examen, models.DO_NOTHING, db_column='id_examen', blank=True, null=True)
    nota = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarioexamen'
