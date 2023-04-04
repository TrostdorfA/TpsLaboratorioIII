import socket
import requests
import json

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server.bind(server_address)

server.listen(2)

while True:
    connection, address = server.accept()
    while True:
            data = connection.recv(1024)
            print('received {0}'.format(data))
            if data:
                print('Enviando de regreso los dato al cliente ')
                Diccionario = json.loads(data.decode('utf-8'))

                texto = r.text.split("\r\n")
                tamaño = len(texto)
                array = texto[(tamaño -2)]

                # if Diccionario == {"temperatura": "", "humedad": ""}: 
                #     Diccionario = {"temperatura": array[18:22], "humedad": array[40:42]}
                # if Diccionario == {"temperatura": ""}: 
                #     Diccionario = {"temperatura": array[18:22]}
                # if Diccionario == {"humedad": ""}:
                #     Diccionario = {"humedad": array[40:42]}
                # else:
                #      print("No se puede realizar la operacion")
                # data = json.dumps(Diccionario)
                # connection.sendall(Diccionario.encode('utf-8'))
                if():
                    data = json.dumps(Diccionario).encode('utf-8')
                    connection.sendall(data)
                if(Diccionario == {"temperatura": ""}):
                    Diccionario['temperatura'] = array[18:22]
                    data = json.dumps(Diccionario).encode('utf-8')
                    connection.sendall(data)
                if(Diccionario == {"humedad": ""}): 
                    Diccionario['humedad'] = array[40:42]
                    data = json.dumps(Diccionario).encode('utf-8')
                    connection.sendall(data)
                if(Diccionario == {"temperatura": "", "humedad": ""}): 
                    Diccionario['temperatura'] = array[18:22]
                    Diccionario['humedad'] = array[40:42]
                    data = json.dumps(Diccionario).encode('utf-8')
                    connection.sendall(data)
            else:
                print('No hay mas datos del cliente')
                break
    connection.close()