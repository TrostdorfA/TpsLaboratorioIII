#
#
import requests
import os

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

#print(r.headers)
#print (r.status_code)
#print(r.encoding)
#print(r.content)
texto = r.text
textoa = texto[-492:-484]
textob = texto[-482:-477]
textoc = texto[-474:-470]
print("Fecha: ", textoa)
print("Hora: ", textob)
print("Temperatura: ", textoc)

#print(texto.split("."))
# print(" ".join(texto.split(" ")))
# textoSplit = (" ".join(texto.split(" ")))
print("<-------Otra forma de hacerlo------->")

texto1 = r.text.split("\r\n")
texto2 = texto1[len(texto1) -2]

print("Fecha: ", texto2[0:8])
print("Hora: ", texto2[10:15])
print("Temperatura: ", texto2[18:22])

texto = r.text.split("\r\n")
tamaño = len(texto)
array = texto[tamaño -2]

Diccionario = {"temperatura": array[18:22], "humedad": array[40:42]}
print(Diccionario)

