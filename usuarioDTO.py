
#*-----------------CLASE DEDICADA AL OBJETO DE TRANSFERENCIA DE DATOS---------------------------
class usuario_DTO:

    #Constructor
    def __init__(self, userID=None, userName=None, puntos=None):
        self._userID=userID
        self._userName=userName
        self._puntos = puntos



    #-----------------------Set y Get para userID-------------------
    @property
    def userID(self):
        return self._userID

    @userID.setter
    def userID(self,nuevo):
        self._userID=nuevo
    #---------------------------------------------------------------


    #----------------------Set y Get para userName------------------
    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self,nuevo):
        self._userName=nuevo
    #---------------------------------------------------------------


    
    
    #-------------Set y Get para los puntos del usuario-------------
    @property
    def puntos(self):
        return self._puntos

    @puntos.setter
    def puntos(self,nuevo):
        self._puntos=nuevo 
    #---------------------------------------------------------------


    #--------------------------Metodo str---------------------------
    def __str__(self):
        sms = f'''
            user id :: {self._userID}
            user name :: {self._userName}
            puntos :: {self._puntos}
        '''
        return sms
    #---------------------------------------------------------------
#*-----------------------------------------------------------------------------------------------




#!-----------------------------------PRUEBAS DEL LA CLASE----------------------------------------
if __name__ == '__main__':
    
    #------------------------INSTANCIAR LA CLASE--------------------
    usuario_X0 = usuario_DTO(userID=34, userName='Kaelthas',puntos=4) 
    #---------------------------------------------------------------

    #------------------Metodos Set y Get para userID-----------------
    print(f'User ID -> {usuario_X0.userID}')
    print('Cambiando el ID ...')
    usuario_X0.userID = 30
    #----------------------------------------------------------------


    #----------------Metodos Set y Get para userName-------------------
    print(f' userName -> {usuario_X0.userName} ')
    print('Cambiando el valor de userName ...')
    usuario_X0.userName = 'elMataSuegrasSengan'
    #-----------------------------------------------------------------


    #-----------------Metodos Set y Get para los puntos-----------------
    print(f'puntos -> {usuario_X0.puntos}')
    print('Cambiando el valor de los puntos...')
    usuario_X0.puntos = 190
    #-----------------------------------------------------------------


    #----------------------------Metodo srt---------------------------
    print(usuario_X0)
    #-----------------------------------------------------------------
#!-----------------------------------------------------------------------------------------------