
nombre = input("ingrese nombre del empleado: ")
horas_trabajadas = float(input("ingrese horas trabajadas: "))
tarifa_horaria = float(input("ingrese tarifa horaria: "))


if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_horaria
else:
    salario_bruto = 35 * tarifa_horaria + (horas_trabajadas - 35) * 1.5 * tarifa_horaria


if salario_bruto <= 2000:
    impuestos = 0
elif salario_bruto <= 2220:
    impuestos = (salario_bruto - 2000) * 0.20
else:
    impuestos = (220 * 0.20) + ((salario_bruto - 2220) * 0.30)


salario_neto = salario_bruto - impuestos


print("nombre:", nombre)
print("horas trabajadas:", horas_trabajadas)
print("tarifa horaria:", tarifa_horaria)
print("salario bruto:", salario_bruto)
print("impuestos:", impuestos)
print("salario neto:", salario_neto)
