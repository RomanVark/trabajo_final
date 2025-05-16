# Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del campus
# Cada laboratorio contiene cinco filas de cuatro computadoras.
# Por cada computadora se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
#valores aleatorios). 
# Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres por laboratorio.

def pedir_ocupacion(fila):
    while True:
        entrada = input("Ingrese el número de computadoras ocupadas en la fila " + str(fila) + " (máx. 4): ")
        try:
            ocupadas = int(entrada)
            if 0 <= ocupadas <= 4:
                print(str(ocupadas) + "/4 ocupadas en la fila " + str(fila))
                return ocupadas
            else:
                print("Error: el número debe estar entre 0 y 4.")
        except:
            print("Error: ingrese solo números enteros.")


# LABORATORIO 1
print("\nLABORATORIO 1\n")
fila1 = pedir_ocupacion(1)
fila2 = pedir_ocupacion(2)
fila3 = pedir_ocupacion(3)
fila4 = pedir_ocupacion(4)
fila5 = pedir_ocupacion(5)

# LABORATORIO 2
print("\nLABORATORIO 2\n")
fila1b = pedir_ocupacion(1)
fila2b = pedir_ocupacion(2)
fila3b = pedir_ocupacion(3)
fila4b = pedir_ocupacion(4)
fila5b = pedir_ocupacion(5)

# LABORATORIO 1 Y 2
total_ocupadas = fila1 + fila2 + fila3 + fila4 + fila5
total_libres = (5 * 4) - total_ocupadas

print("\nResumen LABORATORIO 1:\n")
print("Total ocupadas:", total_ocupadas)
print("Total libres:", total_libres)

total_ocupadas2 = fila1b + fila2b + fila3b + fila4b + fila5b
total_libres2 = (5 * 4) - total_ocupadas2

print("\nResumen LABORATORIO 2:\n")
print("Total ocupadas:", total_ocupadas2)
print("Total libres:", total_libres2)