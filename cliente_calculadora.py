import socket
import sys



cliente_calculadora = socket.socket()
cliente_calculadora.connect( ('192.168.1.45',8080) ) #Se conecta con el servidor_chat
print('Esto es una calculadora virtual, elija una de las siguientes opciones para continuar:')
print('0).Salir del programa.')
print('1).Sumar dos números.')
print('2).Multiplicar dos números.')



repetir = True
while repetir:

##################################################
    opcion = int(input('Introduzca una opcion válida:'))

    if opcion == 0:
        mensaje_opcion = str.encode(str(opcion))
        cliente_calculadora.send(mensaje_opcion)
        print('Usted ha decidido abandonar el programa.')
        sys.exit(1)
    number_1 = float(input('Introduzca el primer valor: '))
    number_2 = float(input('Introduzca el segundo valor: '))
    mensaje_opcion = str.encode(str(opcion))
    mensaje_number_1 = str.encode(str(number_1))
    mensaje_number_2 = str.encode(str(number_2))
                # We must write bytes, not a string
    cliente_calculadora.send(mensaje_opcion)
    cliente_calculadora.send(mensaje_number_1)
    cliente_calculadora.send(mensaje_number_2)
    mensaje_server = cliente_calculadora.recv(1024)#Aquí puedes obtener el mensaje que has escrito en el servidor.
    if opcion == 1:
        print('El resultado de la suma de estos dos números:',number_1,'y',number_2,'es',mensaje_server)
        repetir = True



    elif opcion == 2:
        print('El resultado de la multiplicación de estos dos números:',number_1,'y',number_2,'es',mensaje_server)
        repetir = True
