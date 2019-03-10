import socket
import sys

def IP_PORT():
    IP = input('Introduce una IP: ')
    PORT = int(input('Introduce un PORT: '))
    return IP,PORT

IP,PORT = IP_PORT()

##############################################################
servidor_calculadora = socket.socket()
servidor_calculadora.bind( (IP, PORT) )
servidor_calculadora.listen(5) #He puesto un número arbitrario.

conexion, addr = servidor_calculadora.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
print('Nueva conexión establecida. Se ha iniciado un vínculo.')
print('Esta es la IP del usuario que va a usar la calculadora virtual:',addr)




one = str.encode("1")#Al estar en modo byte es necesario codificarlo para que el programa lo entienda.
two = str.encode("2")
cero = str.encode("0")
repetir = True
while repetir:
    try:

        message_opcion = conexion.recv(1024)
        message_number_1 = conexion.recv(1024).decode('utf-8')
        message_number_2 = conexion.recv(1024).decode('utf-8')

        if message_opcion == one :

            suma = float(message_number_1) + float(message_number_2)
            message_server_suma = str.encode(str(suma)) # es necesario cambiar el tipo float a str

            conexion.send(message_server_suma)

        elif message_opcion == two:

            multiplicacion = float(message_number_1) * float(message_number_2) #tipo float

            message_server_multiplicacion = str.encode(str(multiplicacion)) # es necesario cambiar el tipo float a str

            conexion.send(message_server_multiplicacion)

        elif message_opcion == cero:

            print('El programa finalizará en breve...')
            print('Introduce una nueva IP y su puerto correspondiente.')
            IP,PORT = IP_PORT()

            ##############################################################
            servidor_calculadora = socket.socket()
            servidor_calculadora.bind( (IP, PORT) )
            servidor_calculadora.listen(5) #He puesto un número arbitrario.

            conexion, addr = servidor_calculadora.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
            print('Nueva conexión establecida. Se ha iniciado un vínculo.')
            print('Esta es la IP del usuario que va a usar la calculadora virtual:',addr)

    except KeyboardInterrupt:
        print('El programa se cerrará en breve...')
        sys.exit(1)
