import socket

# Configuración del cliente
host = 'localhost'
port = 8080

# Creación del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexión al servidor
client_socket.connect((host, port))

# Envío de datos al servidor
mi_diccionario = {'temperatura': '', 'humedad': ''}

client_socket.sendall(str(mi_diccionario).encode())
data = client_socket.recv(1024)
print (data)
client_socket.close()