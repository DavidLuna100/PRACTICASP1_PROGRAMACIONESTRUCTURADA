registro_trabajadores = 0
acumulado_sueldos = 0

while True:
    nombre_empleado = input("Ingrese el nombre del trabajador: ")
    horas_laboradas = int(input("Ingrese el número de horas trabajadas: "))
    pago_por_hora = float(input("Ingrese el sueldo por hora: "))

    pago_base = horas_laboradas * pago_por_hora

    if horas_laboradas == 10:
        bono_aumento = pago_base * 0.20
    elif horas_laboradas == 15:
        bono_aumento = pago_base * 0.30
    elif horas_laboradas == 20:
        bono_aumento = pago_base * 0.15
    elif horas_laboradas > 25:
        bono_aumento = pago_base * 0.08
    else:
        bono_aumento = 0

    pago_final_neto = pago_base + bono_aumento

    print("\nTrabajador:", nombre_empleado)
    print("Aumento: $", bono_aumento)
    print("Sueldo neto: $", pago_final_neto)

    registro_trabajadores += 1
    acumulado_sueldos += pago_final_neto

    confirmacion_salida = input("\n¿Desea ingresar otro trabajador? (si/no): ")

    if confirmacion_salida.lower() == "no":
        break

print("\nTotal de trabajadores ingresados:", registro_trabajadores)
print("Monto total de los sueldos netos: $", acumulado_sueldos)