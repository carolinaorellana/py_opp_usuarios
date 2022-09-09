
class Usuario:		# esto es lo que tenemos hasta ahora
    

    #Este es el constructor
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.balance_cuenta = 0


    # agregando el método de depósito
    def hacer_depósito(self, monto):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += monto
    
    def hacer_retiro(self, monto):
        self.balance_cuenta -=monto

    def mostrar_balance_usuario(self):
        print(f"Usuario: " + self.nombre + ", Balance: " + str(self.balance_cuenta))
    
    def transferir_a_usuario(self, monto, usuario):
        self.balance_cuenta -=monto
        usuario.balance_cuenta +=monto
        print(f"Usuario que transfiere: " + self.nombre + ", Balance luego de transferir " + str(monto) + " = " + str(self.balance_cuenta))
        print(f"Usuario que recibe: " + usuario.nombre + ", Balance luego de recibir "+ str(monto) + " = " + str(usuario.balance_cuenta))

carolina = Usuario("Carolina Orellana", "carolina@correo.cl")
maria = Usuario("María Montecino", "maria@correo.cl")
ariel = Usuario("Ariel Reyes", "ariel@correo.cl")

""" 
#imprimir si todo va bien basico
print (carolina.nombre, " : ", carolina.correo)
print (maria.nombre, " : ", maria.correo)
print (ariel.nombre, " : ", ariel.correo)
print (carolina.balance_cuenta)
print (maria.balance_cuenta)
print (ariel.balance_cuenta)
"""

#Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances
#print(carolina.balance_cuenta) #print original de 0

carolina.hacer_depósito(100)
carolina.hacer_depósito(200)
carolina.hacer_depósito(350)
carolina.hacer_retiro(175)

#print(carolina.balance_cuenta)  #print despues de los 3 depositos y un retiro

carolina.mostrar_balance_usuario()

#Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
#print(maria.balance_cuenta) #este es el incial deberia ser 0

maria.hacer_depósito(200)
maria.hacer_depósito(500)
maria.hacer_retiro(50)
maria.hacer_retiro(300)

#print(maria.balance_cuenta)  #este es dsp de las transacciones


maria.mostrar_balance_usuario()

#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
#print(ariel.balance_cuenta)  #este es el incial deberia ser 0

ariel.hacer_depósito(1000)
ariel.hacer_retiro(300)
ariel.hacer_retiro(100)
ariel.hacer_retiro(200)

#print(ariel.balance_cuenta) #este es dsp de las transacciones

ariel.mostrar_balance_usuario()

#BONUS: Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios
carolina.transferir_a_usuario(75, ariel)