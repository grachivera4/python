from sucursal import gestor









if __name__ == '__main__':
    lista = gestor()
    lista.cerear()
    j= True
    i = 7
    while j != False:
        print("que desea realizar: ")
        print("1:cargar datos ")
        print("2:ver dia dela semana, numero de sucursal, importe ")
        print("3:factura total ")
        print("4:que sucursal facturo mas un dia ")
        print("5:sucursal con menos facturacion ")
        print("6:total facturado ")
        print("7:SALIR ")
        i=int(input("elegi: "))
        if(i == 1):
            s = int(input("ingrese numero de sucursal "))
            d = int(input("ingrese numero de dia "))
            imp = float(input(f"ingrese importe de la sucursal {s}, dia {d} "))
            lista.cargar(s,d,imp)
            lista.mostrar()
        if (i == 2):
            s = int(input("ingrese numero de sucursal: "))
            total = lista.total(s)
            print(f"el total acumulado es {total}")  
        if(i == 3):
            d = int(input("ingrese numero de dia: "))
            lista.maximo(d)
        if(i == 5):
            lista.totalsucu()
        if (i == 7):
            j=False
