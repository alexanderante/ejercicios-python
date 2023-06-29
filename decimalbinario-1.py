decimal = int(input("ingrese un numero decimal: "))

binario = ""
while decimal > 0:
    residuo = decimal % 2
    binario = str(residuo) + binario
    decimal = decimal // 2

print("el numero binario equivalente es:", binario)
