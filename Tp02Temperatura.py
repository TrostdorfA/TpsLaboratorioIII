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

texto1 = r.text.split("\r\n")
texto2 = texto1[len(texto1) -2]
print(texto2[0:23])