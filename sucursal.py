class gestor:
    __lista = list
    
    def __init__(self):
        self.__lista = []
        
    def cerear (self):
        # self.__lista=[]
        for i in range (5):
            fila = [0] * 7
            print(fila)
            self.__lista.append(fila)
            
    def cargar(self,s,d,imp):
        self.__lista[s-1][d-1] += imp
        
    def mostrar(self):
        for i in range (5):
            print(self.__lista[i])
            
    def total(self,s):
        acum=0
        for i in range (7):
            acum=acum+self.__lista[s-1][i]
        return acum
    
    def maximo(self,d):
        max=0
        for i in range(5):
            if(self.__lista[i][d-1]>max):
                max = self.__lista[i][d-1]
                indice = i
        print(f"la sucursal que mas recaudo fue {indice}")
        
    def totalsucu(self):
        sucuacum = 0
        for i in range (5):
            sucuacum = sucuacum + self.total(i)
        print(f"el total de todas las sucursales fue {sucuacum}")
        
            
                

            
    
        
        
        
    
    