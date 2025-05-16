# Definimos el número de edificios y días
num_edificios = 4
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_dias = len(dias_semana)
turnos = ["Mañana", "Tarde", "Noche"]

# Inicializamos un diccionario para almacenar el consumo por edificio
consumo_edificios = {}
for i in range(1, num_edificios + 1):
    consumo_edificios[f"Edificio {i}"] = [[0 for _ in range(len(turnos))] for _ in range(num_dias)]

# Registramos el consumo energético
print("Por favor, ingrese el consumo energético en kilovatios (kWh):")
for i in range(1, num_edificios + 1):
    print(f"\nRegistrando consumo para el Edificio {i}:")
    for d_index, dia in enumerate(dias_semana):
        print(f"  Consumo para el día {dia}:")
        for t_index, turno in enumerate(turnos):
            while True:
                try:
                    consumo = float(input(f"    Ingrese el consumo en kWh para el turno de {turno}: "))
                    if consumo >= 0:
                        consumo_edificios[f"Edificio {i}"][d_index][t_index] = consumo
                        break
                    else:
                        print("El consumo debe ser un valor no negativo. Intente de nuevo.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")

# Calculamos el consumo total por edificio y el promedio semanal
total_consumo_por_edificio = {}
promedio_semanal_por_edificio = {}

for edificio, consumo_semanal in consumo_edificios.items():
    total_edificio = 0
    for consumo_dia in consumo_semanal:
        total_edificio += sum(consumo_dia)
    total_consumo_por_edificio[edificio] = total_edificio
    promedio_semanal_por_edificio[edificio] = total_edificio / num_dias

# Mostramos los resultados
print("\n--- Resultados del Consumo Energético Semanal ---")
for edificio, total in total_consumo_por_edificio.items():
    print(f"\nConsumo Total Semanal para {edificio}: {total:.2f} kWh")
    print(f"Promedio de Consumo Diario para {edificio}: {promedio_semanal_por_edificio[edificio]:.2f} kWh")