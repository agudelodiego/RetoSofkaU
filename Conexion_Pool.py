
#---------------------------------Importamos los modulos necesarios-------------------------------
import psycopg2
from psycopg2 import pool
import sys
#-------------------------------------------------------------------------------------------------


#*---------------------------------Creaciond de la clase Conexion_Pool-----------------------------
class Conexion_Pool:

    #--------------------------Variables de clase-----------------------
    _usuario = 'postgres'
    _contraseña = 'admin'
    _host = '127.0.0.1'
    _puerto = '5432'
    _baseDatos = 'RetoSofka'
    _pool = None
    _minConn = 1
    _maxConn = 10
    #-------------------------------------------------------------------


    #----------------------------Obtener un pool------------------------
    @classmethod
    def get_pool(cls):
        
        if cls._pool == None:

            try:
                 
                cls._pool = pool.SimpleConnectionPool(
                    cls._minConn,cls._maxConn,
                    user = cls._usuario,
                    password = cls._contraseña,
                    host = cls._host,
                    port = cls._puerto,
                    database = cls._baseDatos
                )

                # print(f'''
                #                 EL OBJETO POOL FUE CREADO EXITOSAMENTE
                #     --------------------Descripcion del objeto------------------
                #     OBJETO --> {cls._pool}

                #     TIPO --> {type(cls._pool)}
                # ''')
                return cls._pool

            except Exception as error:

                # print(f'''
                #     Error al instancial el objeto pool.
                #     DESCRIPCION: {error}
                #     TIPO: {type(error)}
                # ''')
                sys.exit()

        else:

            print('Devolviendo el objeto Pool ya creado')
            return cls._pool
    #-------------------------------------------------------------------


    #--------------------Solicitar una conexion al pool-----------------
    @classmethod
    def get_conexion(cls):

        #Solicitamos al pool que nos habilite una conexion a la base de datos
        pool_conexiones = cls.get_pool()
        conexion = pool_conexiones.getconn()

        # print(f'''
        #                 OBJETO CONEXION CREADO EXITOSAMENTE
        #     --------------------Descripcion del objeto---------------------
        #     OBJETO --> {conexion}
        #     TIPO --> {type(conexion)}
        # ''')

        return conexion
    #-------------------------------------------------------------------


    #--------------------------Cerrar una conexion----------------------
    @classmethod
    def close_conexion(cls,conexion):

        conn = conexion
        pool_conexiones = cls.get_pool()
        pool_conexiones.putconn(conexion)
        print(f'''
                    OBJETO CONEXION CERRADO EXITOSAMENTE
            Objeto: {conn}
        ''')
    #--------------------------------------------------------------------


    #---------------------Cerrar el pool de conexiones-------------------
    @classmethod
    def close_pool(cls):

        pool_conexiones = cls.get_pool()
        pool_conexiones.closeall()
        print(f'''
            EL OBJETO DE TIPO POOL FUE CERRADO DE MANERA EXITOSA
        ''')
    #--------------------------------------------------------------------
#*-------------------------------------------------------------------------------------------------



#!---------------------------------------ENTORNO DE PRUEBAS-----------------------------------------
if __name__ == '__main__':

    #---------------------Obtener un pool de conexiones------------------
    PosgreSQL_POOL = Conexion_Pool.get_pool()
    print(f'Objeto pool obtenido -> {PosgreSQL_POOL}')
    #--------------------------------------------------------------------


    #--------------------Solicitar una conexion al pool------------------
    conn_1 = Conexion_Pool.get_conexion()
    print(f'Objeto conexion obtenido -> {conn_1}')
    #--------------------------------------------------------------------


    #------------------------Cerrar una conexion-------------------------
    Conexion_Pool.close_conexion(conn_1)
    #--------------------------------------------------------------------


    #--------------------Cerrar el pool de conexiones--------------------
    Conexion_Pool.close_pool()
    #--------------------------------------------------------------------
#!--------------------------------------------------------------------------------------------------