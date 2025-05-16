def pedir_asistencia(secciones, dias_semana):
    asistencia = {}
    for seccion in secciones:
        asistencia[seccion] = {}
        print(f"\nSección {seccion}:")
        for dia in dias_semana:
            print(f"\n  Día: {dia}")
            entrada = input("  Ingrese los nombres de los estudiantes presentes (separados por comas): ").strip()
            while not entrada:
                print(" Entrada vacía. Intente de nuevo.")
                entrada = input("  Ingrese los nombres de los estudiantes presentes (separados por comas): ").strip()
            estudiantes_presentes = [nombre.strip() for nombre in entrada.split(",") if nombre.strip()]
            asistencia[seccion][dia] = estudiantes_presentes
    return asistencia


def mostrar_resumen(asistencia):
    print("\nResumen de asistencia")
    for seccion, dias in asistencia.items():
        print(f"\nSección {seccion}:")
        for dia, estudiantes in dias.items():
            if estudiantes:
                print(f"  {dia}: {', '.join(estudiantes)}")
            else:
                print(f"  {dia}: Nadie presente")


def contar_asistencias(asistencia):
    contador = {}
    for dias in asistencia.values():
        for estudiantes in dias.values():
            for estudiante in estudiantes:
                if estudiante not in contador:
                    contador[estudiante] = 0
                contador[estudiante] += 1
    return contador


if __name__ == "__main__":
    secciones = ['A', 'B', 'C']
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    asistencia = pedir_asistencia(secciones, dias_semana)
    mostrar_resumen(asistencia)

    # Mostrar total de asistencias por estudiante
    totales = contar_asistencias(asistencia)
    print("\nTotal de asistencias por estudiante")
    for estudiante, total in sorted(totales.items()):
        print(f"{estudiante}: {total} asistencias")
