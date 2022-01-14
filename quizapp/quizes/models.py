from django.db import models


class Alternativa(models.Model):
    id_alternativa = models.BigAutoField(primary_key=True)
    id_pregunta = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='id_pregunta', blank=True, null=True)
    mensaje = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'alternativa'


class Comentario(models.Model):
    id_comentario = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='id_publicacion', blank=True, null=True)
    mensaje = models.CharField(max_length=2048)
    puntuacion = models.BigIntegerField()
    foto_solucion = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'comentario'

class Curso(models.Model):
    id_curso = models.BigIntegerField(primary_key=True)
    nombre_curso = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'curso'

class Examen(models.Model):
    id_examen = models.BigAutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    puntaje_max = models.BigIntegerField()
    duracion = models.BigIntegerField()


    class Meta:
        managed = False
        db_table = 'examen'



class Pregunta(models.Model):
    id_pregunta = models.BigAutoField(primary_key=True)
    id_examen = models.ForeignKey(Examen, models.DO_NOTHING, db_column='id_examen', blank=True, null=True)
    id_tipo_pregunta = models.ForeignKey('Tipopregunta', models.DO_NOTHING, db_column='id_tipo_pregunta', blank=True, null=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    puntaje = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pregunta'


class Publicacion(models.Model):
    id_publicacion = models.BigAutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'tipopregunta'

class Universidades(models.Model):
    univ_cod = models.IntegerField(primary_key=True)
    nombre_univ = models.CharField(max_length=25, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    municipio = models.CharField(max_length=2, blank=True, null=True)
    cod_postal = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universidades'


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

