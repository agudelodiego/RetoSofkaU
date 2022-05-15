#-------------------------------------------------Importamos los modulos necesarios----------------------------------------------
from usuarioDTO import*
from Conexion_Pool import*
from Cursor_Conexion import*
import psycopg2
#---------------------------------------------------------------------------------------------------------------------------------


#*-----------------------------------------------Creacion de la clase usuario_DAO-------------------------------------------------
class usuario_DAO:

    #------------------------Atributos de clase----------------------
    _SELECCIONAR = 'SELECT * FROM "usuarios" ORDER BY "puntuacion"'
    _INSERTAR = 'INSERT INTO "usuarios"("userName","puntuacion") VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE "usuarios" SET "userName"=%s,"puntuacion"=%s WHERE "userID"=%s'
    _ELIMINAR = 'DELETE FROM "usuarios" WHERE "userID"=%s'
    #----------------------------------------------------------------


    #-------------------------Metodo selecciona----------------------
    @classmethod
    def seleccionar(cls):

        with Cursor_Conexion() as cursor:

            cursor.execute(cls._SELECCIONAR)
            respuesta = cursor.fetchall()
            personas_BD = []

            for i in respuesta:
                
                pesona_X = usuario_DTO(userID=i[0], userName=i[1], puntos=i[2])
                personas_BD.append(pesona_X)
                print(pesona_X)
            
            return personas_BD
    #----------------------------------------------------------------


    #--------------------------Metodo insertar-----------------------
    @classmethod
    def insertar(cls, userName, puntos):

        with Cursor_Conexion() as cursor:

            persona_X = usuario_DTO(userName=userName, puntos=puntos)
            valores = (userName,puntos)
            cursor.execute(cls._INSERTAR, valores)
            nuevo = cursor.rowcount

            print(f'''
                        REGISTRO INSERTADO CON EXITO
                Registros insertados: {nuevo}
                Registro insertado: {persona_X}
                Tipo de objeto: {type(persona_X)}                
            ''')

            return persona_X
    #----------------------------------------------------------------


    #-------------------------Metodo actualizar----------------------
    @classmethod
    def actualizar(cls, userName, puntos, userID):

        with Cursor_Conexion() as cursor:

            persona_X = usuario_DTO(userName=userName, puntos=puntos, userID=userID)
            valores = (userName, puntos, userID)
            cursor.execute(cls._ACTUALIZAR, valores)
            actualizados = cursor.rowcount

            print(f'''
                        REGISTRO ACTUALIZADO CORRECTAMENTE
                Registros actualizados: {actualizados}
                Registro introducido: {persona_X}
            ''')

            return persona_X
    #----------------------------------------------------------------


    #---------------------------Metodo eliminar----------------------
    @classmethod
    def eliminar(cls, userID):

        with Cursor_Conexion() as cursor:

            valores = (userID,)
            cursor.execute(cls._ELIMINAR, valores)
            eliminados = cursor.rowcount

            print(f'''
                    REGISTRO ELIMINADO EXITOSAMENTE
                Registros eliminados: {eliminados}
            ''')
    #----------------------------------------------------------------
#*-----------------------------------------------------------------------------------------------------------------------------------



#!------------------------------------------------------ENTORNO DE PRUEBAS-----------------------------------------------------------
if __name__ == '__main__':

    #------------------------Prueba metodo seleccionar------------------------
    seleccion1 = usuario_DAO().seleccionar()
    for i in seleccion1:
        print(f'''
            Descripcion del registro
            {i}
        ''')
    #-------------------------------------------------------------------------


    #-------------------------Prueba metodo insertar--------------------------
    insercion1 = usuario_DAO().insertar(userName="jose daniel",puntos=183)
    print(f'''
                    OBJETO INSERTADO EN LA BASE DE DATOS
        Descripcion: {insercion1}
    ''')
    #-------------------------------------------------------------------------


    #--------------------------Prueba metodo actualizar-----------------------
    actualizacon1 = usuario_DAO().actualizar(userName="hola como estas", puntos=9, userID=8)
    print(f'''
                ACTUALIZACION EXITOSA   
        Descripcion: {actualizacon1}
    ''')
    #-------------------------------------------------------------------------


    #---------------------------Prueba metodo eliminar------------------------
    usuario_DAO().eliminar(11)
    #-------------------------------------------------------------------------
#!-----------------------------------------------------------------------------------------------------------------------------------