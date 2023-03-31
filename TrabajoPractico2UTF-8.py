# El objetivo de este trabajo práctico es enviar al servidor un diccionario en formato de bytes que contenga los datos de temperatura y humedad vacíos. Para ello, se debe crear un diccionario con la siguiente estructura:

# mi_diccionario = {"temperatura": "", "humedad": ""}
# La información debe ser obtenida de la estación meteorológica de la facultad y recibir los datos y mostrarlos por ejemplo : La temperatura es 20 ºC y la humedad 70 %.

mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Concordia'}
print(mi_diccionario['nombre']) # salida: 'Juan'
print(mi_diccionario['ciudad']) # salida: 'Juan'
mi_diccionario['edad'] = 26 # modificar valor existente
mi_diccionario['telefono'] = '123-456-7890' # agregar nueva clave-valor
print(mi_diccionario) # salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Concordia', 'telefono': '123-456-7890'}