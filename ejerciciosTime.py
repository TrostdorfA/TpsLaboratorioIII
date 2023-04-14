# Ejercicios prácticos con el módulo time (nivel difícil)
# 1 Escribe una función que tome como entrada una fecha en formato dd/mm/aaaa y calcule el día de la semana correspondiente (por ejemplo, "lunes", "martes", etc.) utilizando el módulo time.

print("<--------Ejercicio1-------->")
def dia_semana(fecha):
    import time
    fecha = time.strptime(fecha, "%d/%m/%Y")
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return dias[fecha.tm_wday]

print(dia_semana("01/01/2020"))
print(dia_semana("02/01/2020"))

# 2 Escribe una función que tome como entrada una fecha en formato dd/mm/aaaa y calcule el número de días que han pasado desde esa fecha hasta la fecha actual.

print("<--------Ejercicio2-------->")
def dias_pasados(fecha):
    import time
    fecha = time.strptime(fecha, "%d/%m/%Y")
    fecha_actual = time.localtime()
    return (time.mktime(fecha_actual) - time.mktime(fecha)) // 86400

print(dias_pasados("01/01/2020"))
print(dias_pasados("02/01/2020"))

# 3 Escribe una función que tome como entrada una fecha en formato dd/mm/aaaa y calcule el número de segundos que han pasado desde esa fecha hasta la fecha actual.

print("<--------Ejercicio3-------->")
def segundos_pasados(fecha):
    import time
    fecha = time.strptime(fecha, "%d/%m/%Y")
    fecha_actual = time.localtime()
    return time.mktime(fecha_actual) - time.mktime(fecha)

print(segundos_pasados("01/01/2020"))
print(segundos_pasados("02/01/2020"))

print("<--------EjemploPythonTime-------->")

import time

# Obtener el tiempo actual en segundos desde la época de Unix
tiempo_actual = time.time()
print(f"Tiempo actual en segundos desde la época de Unix: {tiempo_actual}")

# Esperar 2 segundos
print("Esperando 2 segundos...")
time.sleep(2)
print("¡Listo!")

# Convertir el tiempo actual en UTC
tiempo_utc = time.gmtime(tiempo_actual)
print(f"Tiempo actual en UTC: {time.strftime('%Y-%m-%d %H:%M:%S', tiempo_utc)}")

# Convertir el tiempo actual en la zona horaria local
tiempo_local = time.localtime(tiempo_actual)
print(f"Tiempo actual en la zona horaria local: {time.strftime('%Y-%m-%d %H:%M:%S', tiempo_local)}")
print(tiempo_local)

print("<--------OtrosEjerciciosTime-------->")
# Ejercicios prácticos con el módulo time
# Fácil: Escribe un programa que muestre la fecha y hora actual en el siguiente formato: dd/mm/aaaa hh:mm:ss.

def fecha_hora():
    import time
    fecha = time.localtime()
    return time.strftime("%d/%m/%Y %H:%M:%S", fecha)

print(fecha_hora())

# Intermedio: Escribe una función que tome como entrada dos fechas en formato dd/mm/aaaa y calcule la cantidad de días transcurridos entre ambas fechas.

def fechas(fecha1, fecha2):
    import time
    fecha1 = time.strptime(fecha1, "%d/%m/%Y")
    fecha2 = time.strptime(fecha2, "%d/%m/%Y")
    return (time.mktime(fecha2) - time.mktime(fecha1)) // 86400

print(fechas("01/01/2020", "30/10/2020"))

# Difícil: Escribe una función que tome como entrada una lista de fechas en formato dd/mm/aaaa y devuelva la fecha que ocurrió con mayor frecuencia. Si hay varias fechas que ocurren con la misma frecuencia máxima, devuelve la fecha más reciente.

def fecha_mas_frecuente(lista_fechas):
    import time
    fechas = {}
    for fecha in lista_fechas:
        fecha = time.strptime(fecha, "%d/%m/%Y")
        if fecha in fechas:
            fechas[fecha] += 1
        else:
            fechas[fecha] = 1
    return max(fechas, key=fechas.get)


print(f"Fecha mas frecuente convertida a UTC: {time.strftime('%Y-%m-%d %H:%M:%S', fecha_mas_frecuente(['01/01/2020', '01/01/2020', '01/01/2020', '02/01/2020', '02/01/2020', '03/01/2020']))}")