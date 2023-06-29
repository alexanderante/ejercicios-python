numero_decimal = int(input("ingrese un numero decimal: "))
binario = ""
cociente = numero_decimal
while cociente > 0:
    resto = cociente % 2
    binario = str(resto) + binario
    cociente //= 2
octal = ""
cociente = numero_decimal
while cociente > 0:
    resto = cociente % 8
    octal = str(resto) + octal
    cociente //= 8

hexadecimal = ""
cociente = numero_decimal
while cociente > 0:
    resto = cociente % 16
    if resto < 10:
        hexadecimal = str(resto) + hexadecimal
    else:
        hexadecimal = chr(resto + 55) + hexadecimal
    cociente //= 16

print(numero_decimal, "(decimal) = ", binario, "(binario) = ", octal, "(octal) = ", hexadecimal, "(hexadecimal)")
