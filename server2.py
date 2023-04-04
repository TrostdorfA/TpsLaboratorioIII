import socket


def str2dict(_str) -> str:
    _dict = {}      
    for bloke in _str.split(', '):
        k,v =  bloke.split(': ')
        _dict[k[1:-1]] = v[1:-1]  
    return _dict

def proc(_dict)-> dict:
    if 'temperatura' in _dict:
        _dict['temperatura'] = '32'
    if 'humedad' in _dict:
        _dict['humedad'] = '75'
    return str(_dict)

def main():

    server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
    server_address = ('localhost', 8080)
    server.bind(server_address)

    server.listen(3)
    _bytes = bytes()

    while True:
        try:
            connection, address = server.accept()
            while connection != None :
                try: 
                    data = connection.recv(1024)
                    if data:
                        _bytes += data
                        _dict = str2dict(_bytes.decode()[1:-1])
                        connection.sendall(proc(_dict).encode())
                        print('Datos: {0} de {1}'.format(proc(_dict), address))    

                    else:
                        #print('Datos: {0} de {1}'.format(_bytes.decode(), address))
                        del _bytes
                        _bytes = bytes()
                        connection.close()
                        connection = None
                        break
                except socket.error as e:
                    print(e)  
        except KeyboardInterrupt:
            print("Exit server...")
            exit(0)


if __name__ == "__main__":
    main()