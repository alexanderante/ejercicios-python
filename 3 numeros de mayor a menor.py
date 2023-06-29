
numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))
numero3 = int(input("ingresa el tercer numero: "))

# Ordenar los numeros de mayor a menor
if numero1 < numero2:
    numero1, numero2 = numero2, numero1
if numero1 < numero3:
    numero1, numero3 = numero3, numero1
if numero2 < numero3:
    numero2, numero3 = numero3, numero2

print("los numeros ingresados son", numero1, ",", numero2, "y", numero3, "y organizados de forma descendente son", numero1, ",", numero2, ",", numero3)
