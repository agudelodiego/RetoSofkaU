
#*-------------Creacion de la calse encargada de crar objeto de transferencia de datos, pero esta vez para las preguntas----------------------------
class Preguntas_DTO:

    #-----------------------------------Metodo constructor----------------------------
    def __init__(self, idPregunta=None, dificualtad=None, pregunta=None, respuestaCorrecta=None, respuesta2=None, respuesta3=None, respuesta4=None):
        self._idPregunta = idPregunta
        self._dificualtad = dificualtad
        self._pregunta = pregunta
        self._respuestaCorrecta = respuestaCorrecta
        self._respuesta2 = respuesta2
        self._respuesta3 = respuesta3
        self._respuesta4 = respuesta4
    #------------------------------------------------------------------------------------


    #----------------------------Get y Set para idPregunta-------------------------------
    @property
    def idPregunta(self):
        return self._idPregunta

    @idPregunta.setter
    def idPregunta(self,nuevo):
        self._idPregunta = nuevo
    #--------------------------------------------------------------------------------------


    #-------------------Get y Set para la dificultad de la pregunta------------------------
    @property
    def dificualtad(self):
        return self._dificualtad

    @dificualtad.setter
    def dificualtad(self,nuevo):
        self._dificualtad=nuevo
    #--------------------------------------------------------------------------------------
    
    
    #-----------------------Get y Set para la pregunta en si misma--------------------------
    @property
    def pregunta(self):
        return self._pregunta

    @pregunta.setter
    def pregunta(self,nuevo):
        self._pregunta = nuevo
    #---------------------------------------------------------------------------------------


    #-------------Get y Set para la respuesta CORRECTA de la pregunta-----------------------
    @property
    def respuestaCorrecta(self):
        return self._respuestaCorrecta
    @respuestaCorrecta.setter
    def respuestaCorrecta(self,nuevo):
        self._respuestaCorrecta = nuevo
    #---------------------------------------------------------------------------------------


    #-------------Get y Set para la segunda respuesta(respuesta errada)--------------------
    @property
    def respuesta2(self):
        return self._respuesta2

    @respuesta2.setter
    def respuesta2(self,nuevo):
        self._respuesta2 = nuevo
    #--------------------------------------------------------------------------------------


    #-------------Get y Set para la tercera respuesta(respuesta errada)--------------------
    @property
    def respuesta3(self):
        return self._respuesta3

    @respuesta3.setter
    def respuesta3(self,nuevo):
        self._respuesta3 = nuevo
    #--------------------------------------------------------------------------------------



    #-------------Get y Set para la cuarta respuesta(respuesta errada)---------------------
    @property
    def respuesta4(self):
        return self._respuesta4

    @respuesta4.setter
    def respuesta4(self,nuevo):
        self._respuesta4 = nuevo
    #-------------------------------------------------------------------------------------



    #--------------------------------------Metodo str-------------------------------------
    def __str__(self):

        #Agregaremos mas opciones
        sms = f'''
            {self._pregunta}:
            a -> {self._respuestaCorrecta}
            b -> {self._respuesta2}
            c -> {self._respuesta3}
            d -> {self._respuesta4}
            e -> SALIR
        '''
        return sms
    #------------------------------------------------------------------------------------
    
#*--------------------------------------------------------------------------------------------------------------------------------------------------


#!-------------------------------------------------Pruebas de instanciamiento de la clase----------------------------------------------------------
if __name__ == "__main__":

    preguntas_X = Preguntas_DTO(3,"nivel 2","que hora es ?", "4am","3pm", "5am", "8am")
    print(preguntas_X)

#!------------------------------------------------------------------------------------------------------------------------------------------------