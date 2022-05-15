#-----------------Modulos importantes----------------
from usuarioDAO import*
from usuarioDTO import*
from PreguntasDAO import*
import random
#---------------------------------------------------


#*--------------------------------------Creacion de la calse juego, la cual le brinda funcionalidades al juego--------------------------------------------
class Juego:

    _ronda = "Nivel 1"  #! El juego tendra 5 rondas e iniciara por defecto en la primera
    _puntuacion = 0  #! El usuario inicia con una puntuacion de 0
    _usuario = None  #* Usuario que se encuentra jugando al juego de trivia en este momento
    _pregunta = None


    #-------Metodo encargado de verificar un usuario en la base de datos(interactua con el objeto de acceso a datos)-------
    @classmethod
    def validar_usuarios(cls,nombre):

        #Consulta de seleccion a la base de dato para obtener los usuario existentes(Develve una lista con objetos de tipo usuario)
        cantidadUsuarios = usuario_DAO().seleccionar()
        variable_aux = ""

        for i in cantidadUsuarios:

            if nombre==i.userName:

                #Si el usario existe dentro de la base de datos lo retorna(interactua con el objeto de transferencia de datos)
                variable_aux = i
                # print(f'''
                #     EJECUCION DEL IF
                #     nom -> {i.userName} Tipo -> {type(i.userName)}
                #     nombre -> {nombre} Tipo -> {type(nombre)}
                # ''')
                break

            else:

                #Si el usuario no  existe dentro de la base de datos retorna Falso
                variable_aux = False

        return variable_aux
    #----------------------------------------------------------------------------------------------------------------------



    #------Metodo encargado de agregar a un nuevo usuario a la base de datos(interactua con el objeto de acceso a datos haciendo una consulta de insercion)------
    @classmethod
    def nuevo_usuario(cls,nombre):

        #Llamamos al metodo encargado de validar los usuarios
        respuesta = cls.validar_usuarios(nombre)
        print(f'''
            Respuesta ingresada {respuesta}
        ''')

        if respuesta == False:

            #Una vez que el usuario fue creado, seteamos la variable de clase _usuario y la retornamos
            cls._usuario = usuario_DAO().insertar(userName=nombre,puntos=0)
            print("Usuario creado exitosamente")
            return cls._usuario

        else:

            print("Ese nombre de usuario ya esta siendo utlizado por otra persona, por favor seleccione otro nombre")
            return False
    #------------------------------------------------------------------------------------------------------------------------------------------------------------



    #--------------Metodo encargado de validar a un usuario existente-----------------------
    @classmethod
    def existente_usuario(cls,nombre):

        #Llamamos al metodo encargado de verificar un usuario dentro de la base de datos
        respuesta = cls.validar_usuarios(nombre)

        if respuesta == False:

            print(f"El usuario {nombre}, no existe.")
            return False

        else:

            #Si el usuario ya existe iguala la variable de clase _usuarios lo que devuelve el metodo(devuelve el objeto usuario)
            cls._usuario = respuesta
            return cls._usuario
    #-----------------------------------------------------------------------------------------


    #----------Metodo encargado de actualizar la puntuacion del usario dentro de la base de datoss-----------
    @classmethod
    def puntuacion(cls,puntos):

        #Si el usuario no esta definido mostramos informacion al usuario
        if cls._usuario == None:

            print("Ha ocurrido un error, no se puede actualizar la puntuacion")

        #Si la variable usuario si se encuentra definida, actualizamos los puntos asociados al usuario en la base de datos
        else:

            cls._puntuacion = puntos
            cls._usuario.puntos(puntos)
            usuario_DAO().actualizar(cls._usuario.userName, cls._puntuacion, cls._usuario.userID)
    #-------------------------------------------------------------------------------------------------------



    #----------Metodo encargado de mostrar la pregunta de forma aleatoria correspondiente a la ronda en que se encuentre el usuario-------------
    @classmethod
    def pregunta_aleatoria(cls):

        #Llamamos al metoodo encargado de devolver las preguntas del nivel deseado
        respuesta_bancoPreguntas = Preguntas_DAO().seleccionar(cls._ronda)
        
        #Averiguamos el tamaño del objeto
        tamaño = len(respuesta_bancoPreguntas)

        #Genramos un numero aleatorio
        numero_aleatorio = random.randrange(0,tamaño-1)
        # print(f'''
        #     numero aleatorio -> {numero_aleatorio}
        # ''')

        #Seleccionamos la pregunta que le enviaremos al usuario mediante el numero aleatorio
        objeto_pregunta = respuesta_bancoPreguntas[numero_aleatorio]
        # print(f'''
        #     Pregunta para el usuario:
        #     {objeto_pregunta}
        # ''')

        #Retornamos el objeto pregunta
        return objeto_pregunta

    #-------------------------------------------------------------------------------------------------------------------------------------------

#*--------------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------Creamos el programa que interactua con el usuario-----------------------------------
#flag = 1 -> indica que el usuario
flag = 1

while flag < 5:
    
    #Si _falg vale el uno le pedimos al usuario que se registre o que acceda a su usuario
    if flag == 1:

        print(f'''
            Hola Usuario, bienvenido al juego de trivia. Accede con tu nombre de usuario o crea un nuevo usuairo, ingresa la opcion deseada
            1 -> Ingresar con un usuario existente
            2 -> Crear un nuevo usuario
        ''')
        opcion_usuario = input("Ingrese la respuesta : ")
        print(f'''
            Usted ha seleccionado la opcion {opcion_usuario}
        ''')

        if opcion_usuario == '1':

            nombre_ingresado = input("Ingrese el un nick name: ")

            #Solicitamos al metodo existente_usuario que nos valide al usuario
            respuesta = Juego().existente_usuario(nombre_ingresado)
            print(f''''
                La respuesta de fue {respuesta}
            ''')
            if respuesta == False:

                print(f'''
                    {respuesta} no existen dentro de la base de datos.
                ''')

            else:

                print(f'''
                    Usuario registrado correctamente bienvenido de nuevo {respuesta.userName}
                ''')
                flag = 2
                print(flag)

        elif opcion_usuario == '2':

            nombre_ingresado = input("Ingrese un nuevo nickName: ")

            #Verificamos que el nombre de usuario no exista aun dentro de la base de datos
            respuesta = Juego().nuevo_usuario(nombre_ingresado)
            print(f'''
                Respuesta {respuesta}
            ''')
            if respuesta == False:
                print("Por favor vuelva a intentarlo")

            else:
                print(f'''
                    Bienvenido al juego de trivia {respuesta.userName}
                ''')
                flag = 2

    #! PARA DESPUES
    elif flag == 2:
        pass    
    
        

#-----------------------------------------------------------------------------------------------------------------------


#!----------------------------------------------Entorno de pruebas------------------------------------------------------
# if __name__ == "__main__":

#     variable_prueba = Juego().pregunta_aleatoria()
#     print(variable_prueba)

#     variable_prueba = Juego().validar_usuarios("hola como e")
#     print(variable_prueba)
#!----------------------------------------------------------------------------------------------------------------------