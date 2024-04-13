class CajaDeAhorro:
    __nrocta=str
    __cuil=str
    __apellido=str
    __nombre=str
    __saldo=float
    def __init__(self,nrocta,cuil,apellido,nombre,saldo):
        self.__nroCta = nrocta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo
    def mostrardatos(self):
        print(self.__nrocta,self.__cuil,self.__apellido,self.__nombre,self.__saldo)
    def extraerimporte(self,importe):
        self.__importe = importe
        self.__saldo = self.__saldo - self.__importe
    def depositar(self,valor):
        if valor>0:
            self.__valor = valor
            self.__saldo = self.__saldo + valor
        else:
                print("no es posible ")
    #def validarCUIL(self)



if __name__ == '__main__':
    unacaja = CajaDeAhorro("5000000","274000","lujan","Gracho",2837)
    #otracaja=CajaDeAhorro("80000000","2785889","Vargas","Vera","3838")
    unacaja.mostrardatos()
    unacaja.extraerimporte(600)
    unacaja.mostrardatos()
    valor = float(input("ingrese valor a depositar "))
    unacaja.depositar(valor)
    unacaja.mostrardatos()
    


