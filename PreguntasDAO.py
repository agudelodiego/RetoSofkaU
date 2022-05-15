#-------------Modulos necesarios--------------------
from usuarioDTO import*
from Conexion_Pool import*
from Cursor_Conexion import*
from PreguntasDTO import*
import psycopg2
#---------------------------------------------------



#! IMPORTANTE: Dese aca solo es posible realizar consultas de seleccion a la base de datos



#*---------------------------------Clase dedicada al objeto de acceso a dato pero para el banco de preguntas-----------------------------------
class Preguntas_DAO:

    
    _SELECCIONAR = 'SELECT * FROM "preguntas" WHERE "dificultad"=%s'


    #-------------Consulta de seleccion a al base de datos para obtener todas las preguntas----------
    @classmethod
    def seleccionar(cls,nivel):

        with Cursor_Conexion() as cursor:

            cursor.execute(cls._SELECCIONAR,(nivel,))
            respuesta = cursor.fetchall()
            preguntasBanco = []

            for i in respuesta:
                pregunta_X = Preguntas_DTO(idPregunta=i[0], dificualtad=i[1], pregunta=i[2], respuestaCorrecta=i[3], respuesta2=i[4], respuesta3=i[5], respuesta4=i[6])
                preguntasBanco.append(pregunta_X)
                #print(pregunta_X)
            
            return preguntasBanco
    #-----------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------------



#!------------------------------------------------Prueba del funcionamiento del modulo-----------------------------------------------------------
if __name__ == "__main__":

    respuestaBDD = Preguntas_DAO().seleccionar("Nivel 1")

    print(f'''
        Conexion al banco de preguntas realizado exitosamente
        Objeto -> {respuestaBDD}
        Tamaño -> {len(respuestaBDD)}
        Tipo -> {type(respuestaBDD)}
        Iteracion de la lista obtenida
    ''')
    for i in respuestaBDD:
        print(i.dificualtad)

#!-----------------------------------------------------------------------------------------------------------------------------------------------