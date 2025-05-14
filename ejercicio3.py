#control de ventas en la feria universitaria
# Definicion de variables
total_feria = 0
total_dia = 0
stands = ["stand1", "stand2", "stand3", "stand4"]#deifinicion de stands
dias = ["miercoles", "jueves", "viernes"] #dias de la feria
productos = ["producto1", "producto2", "producto3", "producto4"] #productos a vender
#ingreso de ventas por stand
for stand in stands:
    print(f"Ingrese las ventas del {stand} por dia")
    for dia in dias:
        print(f"Ingrese las ventas del {dia}")
        venta = float(input())
        total_dia += venta
        total_feria += venta
    print(f"Total de ventas del {stand}: {total_dia}")
    total_dia = 0