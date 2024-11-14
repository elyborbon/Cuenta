
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def info(self):
        print ("Selecciona la actividad que desea realizar.")
        print ("Pulsa 1. Si desea informacion de la cuenta.")
        print ("Pulsa 2. Si desea ingresar.")
        print ("Pulsa 3. Si desea retirar efectivo.")

        accion = int (input("Selecciona la opcion: "))
        if accion ==1:
            Cuenta.mostrar(self)
            
        elif accion ==2:
            Cuenta.ingresar(self)
        elif accion ==3:
            Cuenta.retirar(self)
        else:
            print ("SALIR")


    def opcion(self):
        print ("Desea ver mas informacion? :  ")
        print ("Coloca: yes, si quieres mas informacion")
        print ("Coloca: no, para finalizar programa")
        informacion = input()
        
        if informacion =="yes":
            Cuenta.info(self)
        else:
            print("Finalizar programa")

    def mostrar(self):
        print ("CUENTA: ")
        print ("El titular de la cuenta es: {} y cuenta con  {} pesos ".format(self.titular, self.cantidad))
        Cuenta.opcion(self)

    def ingresar (self):
        cantidad_introducir = int (input ("Cuanto desea ingresar ?  "))
        if cantidad_introducir > 0:
            Sumatoria= cantidad_introducir + self.cantidad
            print ("Ahora tienen la cantidad de {} pesos en su cuenta".format(Sumatoria))
            Cuenta.opcion(self)

    def retirar(self):
        cantidad_retirar = int (input ("Cuanto desea retirar ?  "))
        if cantidad_retirar > 0:
            Restar= self.cantidad - cantidad_retirar 
            print ("Ahora tienen la cantidad de {} pesos en su cuenta".format(Restar))
            Cuenta.opcion(self)

Cuenta1 = Cuenta("Mario Medina", 500)
Cuenta1.info()