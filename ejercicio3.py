#control de ventas en la feria universitaria
# Definición de variables
total_feria = 0
stands = ["stand1", "stand2", "stand3", "stand4"]  # definición de stands
dias = ["miercoles", "jueves", "viernes"]  # días de la feria
productos = ["producto1", "producto2", "producto3"]  # 3 productos por stand

#ingreso de ventas por dias
for dia in dias:
    print(f"\ningrese las ventas del {dia}")
    total_dia = 0
    #ingreso de ventas por stand
    for stand in stands:
        print(f"\ningrese las ventas del {stand}")
        total_stand = 0
        #ingreso de ventas por producto
        for producto in productos:
            venta = float(input(f"ingrese la venta del {producto}:"))
            total_stand += venta
        #calculo de total por stand
        print(f"\ntotal de ventas del {stand}: {total_stand}")
        total_dia += total_stand
    #calculo de total por dia
    print(f"\ntotal de ventas del {dia}: {total_dia}")
    total_feria += total_dia
#calculo de total de la feria
print(f"\ntotal de ventas de la feria: {total_feria}")