  
decimal = int(input("ingresa un numero decimal: "))
binario = bin(decimal)[2:]
print("el numero binario equivalente es:", binario)

binario = input("ingresa un numero binario: ")
decimal = int(binario, 2)
print("el numero decimal equivalente es:", decimal)

decimal = int(input("ingresa un numero decimal: "))
binario = bin(decimal)[2:]
octal = oct(decimal)[2:]
hexadecimal = hex(decimal)[2:]

print("el numero binario equivalente es:", binario)
print("el numero octal equivalente es:", octal)
print("el numero hexadecimal equivalente es:", hexadecimal)

numero1 = float(input("ingresa el primer numero: "))
numero2 = float(input("ingresa el segundo numero: "))
numero3 = float(input("ingresa el tercer numero: "))

suma = numero1 + numero2 + numero3
promedio = suma / 3

print("la suma de los tres numeros es:", suma)
print("el promedio de los tres numeros es:", promedio)
