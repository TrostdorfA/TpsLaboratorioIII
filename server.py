import socket
import requests
import json

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("0.0.0.0",8080))

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
                array = texto[tamaño -2]

                Diccionario = {"Temperatura": array[18:22], "Humedad": array[40:42]}
                data = json.dumps(Diccionario)
                connection.sendall(Diccionario.encode('utf-8'))
            else:
                print('No hay mas datos del cliente')
                break
    connection.close()