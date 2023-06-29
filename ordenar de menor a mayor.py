
numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))

# Ordenar los números de menor a mayor

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print("los numeros ingresados son", numero1, "y", numero2, "y organizados son", numero1, ",", numero2)
